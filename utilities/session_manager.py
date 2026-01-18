"""Session Cookie Manager for reusing browser sessions.

Responsibility:
- Persist session cookies to local storage
- Load cookies from storage on startup
- Handle cookie expiration and freshness
- Fall back gracefully to fresh sessions
- Support both local and CI/CD environments

This utility ONLY handles cookie storage/retrieval.
It does NOT:
- Perform assertions
- Handle authentication logic
- Manage test state
- Know about pages or flows
"""

import os
import pickle
import json
from pathlib import Path
from datetime import datetime, timedelta
from utilities.customLogger import LoggerFactory


logger = LoggerFactory.get_logger(__name__)


class SessionManager:
    """Manages session cookie persistence and reuse across test runs."""
    
    # Default cookie storage location
    COOKIE_DIR = Path(__file__).parent.parent / ".session_cookies"
    COOKIE_FILE = COOKIE_DIR / "session_cookies.pkl"
    METADATA_FILE = COOKIE_DIR / "session_metadata.json"
    
    # Cookie freshness - if cookies are older than this, request fresh session
    COOKIE_MAX_AGE_HOURS = 24
    
    def __init__(self, driver=None):
        """Initialize SessionManager.
        
        Args:
            driver: Optional Selenium WebDriver instance for cookie operations
        """
        self.driver = driver
        self._ensure_storage_dir()
    
    @classmethod
    def _ensure_storage_dir(cls):
        """Ensure cookie storage directory exists."""
        try:
            cls.COOKIE_DIR.mkdir(parents=True, exist_ok=True)
            logger.debug(f"Cookie storage directory ready: {cls.COOKIE_DIR}")
        except Exception as e:
            logger.warning(f"Could not create cookie directory: {str(e)}")
    
    def cookies_exist(self):
        """Check if valid session cookies exist in storage.
        
        Returns:
            bool: True if cookies exist and are fresh, False otherwise
        """
        if not self.COOKIE_FILE.exists():
            logger.debug("No cookie file found")
            return False
        
        # Check metadata for freshness
        if not self._is_cookie_fresh():
            logger.info("Stored cookies are too old - requesting fresh session")
            self._delete_cookies()
            return False
        
        logger.info("Valid session cookies found in storage")
        return True
    
    def _is_cookie_fresh(self):
        """Check if stored cookies are fresh (not expired).
        
        Returns:
            bool: True if cookies are recent, False if expired or missing
        """
        if not self.METADATA_FILE.exists():
            logger.debug("No metadata file found - cookies considered stale")
            return False
        
        try:
            with open(self.METADATA_FILE, 'r') as f:
                metadata = json.load(f)
            
            saved_time_str = metadata.get('saved_at')
            if not saved_time_str:
                logger.debug("No timestamp in metadata - cookies considered stale")
                return False
            
            saved_time = datetime.fromisoformat(saved_time_str)
            cookie_age = datetime.now() - saved_time
            max_age = timedelta(hours=self.COOKIE_MAX_AGE_HOURS)
            
            if cookie_age > max_age:
                logger.info(f"Cookies are {cookie_age.total_seconds() / 3600:.1f}h old "
                          f"(max allowed: {self.COOKIE_MAX_AGE_HOURS}h)")
                return False
            
            logger.debug(f"Cookies are fresh ({cookie_age.total_seconds() / 3600:.1f}h old)")
            return True
            
        except Exception as e:
            logger.warning(f"Error checking cookie freshness: {str(e)}")
            return False
    
    def load_cookies(self, driver):
        """Load cookies from storage into WebDriver instance.
        
        Args:
            driver: Selenium WebDriver instance
            
        Returns:
            bool: True if cookies were loaded successfully, False otherwise
        """
        if not self.COOKIE_FILE.exists():
            logger.debug("No cookies to load - fresh session will be created")
            return False
        
        try:
            with open(self.COOKIE_FILE, 'rb') as f:
                cookies = pickle.load(f)
            
            logger.info(f"Loading {len(cookies)} stored cookies into driver")
            
            for cookie in cookies:
                try:
                    # Remove problematic cookie attributes that can cause issues
                    # when reinserting (expiry might be in the past)
                    cookie_copy = cookie.copy()
                    
                    # Set expiry to future if it exists
                    if 'expiry' in cookie_copy:
                        # Extend expiry to 24 hours from now
                        cookie_copy['expiry'] = int((datetime.now() + timedelta(hours=24)).timestamp())
                    
                    driver.add_cookie(cookie_copy)
                    
                except Exception as cookie_error:
                    logger.warning(f"Could not add cookie '{cookie.get('name', 'unknown')}': "
                                 f"{str(cookie_error)[:80]}")
            
            logger.info("Cookies loaded successfully")
            return True
            
        except Exception as e:
            logger.error(f"Error loading cookies: {str(e)}")
            self._delete_cookies()
            return False
    
    def save_cookies(self, driver):
        """Save current session cookies to storage.
        
        Args:
            driver: Selenium WebDriver instance to get cookies from
            
        Returns:
            bool: True if cookies were saved successfully, False otherwise
        """
        try:
            cookies = driver.get_cookies()
            
            if not cookies:
                logger.warning("No cookies to save")
                return False
            
            logger.info(f"Saving {len(cookies)} session cookies to storage")
            
            # Save cookies to file
            with open(self.COOKIE_FILE, 'wb') as f:
                pickle.dump(cookies, f)
            
            # Save metadata
            metadata = {
                'saved_at': datetime.now().isoformat(),
                'cookie_count': len(cookies),
                'environment': 'ci' if self._is_ci_environment() else 'local'
            }
            
            with open(self.METADATA_FILE, 'w') as f:
                json.dump(metadata, f, indent=2)
            
            logger.info(f"Cookies saved to {self.COOKIE_FILE}")
            return True
            
        except Exception as e:
            logger.error(f"Error saving cookies: {str(e)}")
            return False
    
    def _delete_cookies(self):
        """Delete stored cookies and metadata files."""
        try:
            if self.COOKIE_FILE.exists():
                self.COOKIE_FILE.unlink()
                logger.debug(f"Deleted cookie file: {self.COOKIE_FILE}")
            
            if self.METADATA_FILE.exists():
                self.METADATA_FILE.unlink()
                logger.debug(f"Deleted metadata file: {self.METADATA_FILE}")
                
        except Exception as e:
            logger.warning(f"Error deleting stored cookies: {str(e)}")
    
    def clear_cookies(self, driver):
        """Clear all cookies from current driver session.
        
        Args:
            driver: Selenium WebDriver instance
        """
        try:
            driver.delete_all_cookies()
            logger.debug("All cookies cleared from current driver session")
        except Exception as e:
            logger.warning(f"Error clearing driver cookies: {str(e)}")
    
    @staticmethod
    def _is_ci_environment():
        """Detect if running in CI/CD environment.
        
        Returns:
            bool: True if running in GitLab CI or similar CI system
        """
        ci_vars = ['CI', 'GITLAB_CI', 'GITHUB_ACTIONS', 'JENKINS_URL', 'CI_COMMIT_SHA']
        return any(var in os.environ for var in ci_vars)
    
    @staticmethod
    def get_cookie_dir():
        """Get the cookie storage directory path.
        
        Returns:
            Path: Directory where cookies are stored
        """
        return SessionManager.COOKIE_DIR
