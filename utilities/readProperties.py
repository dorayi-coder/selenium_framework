import configparser
import os
from pathlib import Path


class ReadProperties:
    """Read configuration from config.ini with environment variable override support.
    
    Priority order (highest to lowest):
    1. Environment variables (for CI/CD override)
    2. config.ini values
    
    This allows:
    - Local testing with config.ini
    - CI/CD override via GitHub Actions secrets
    - Docker compose environment variables
    """
    
    def __init__(self):
        self.config = configparser.ConfigParser()
        # Find config.ini in Configurations folder
        config_path = self._find_config_file()
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"config.ini not found at {config_path}")
        self.config.read(config_path)
    
    def _find_config_file(self):
        """Locate config.ini in Configurations folder.
        
        Searches:
        1. Current directory/Configurations/config.ini
        2. Parent directory/Configurations/config.ini
        3. Two levels up/Configurations/config.ini
        """
        # Method 1: Relative to this utilities file
        file_dir = Path(__file__).resolve().parent.parent
        config_path = file_dir / "Configurations" / "config.ini"
        if config_path.exists():
            return str(config_path)
        
        # Method 2: Check current working directory
        alt_path = Path.cwd() / "Configurations" / "config.ini"
        if alt_path.exists():
            return str(alt_path)
        
        # Fallback path (will raise error if not found)
        return str(file_dir / "Configurations" / "config.ini")
    
    def get_base_url(self):
        """Get base URL with environment variable override.
        
        Returns:
            str: Base URL from env var (BASE_URL) or config.ini
            
        Example:
            - Locally: http://localhost:5000
            - CI/CD: https://staging.example.com (via BASE_URL env var)
        """
        return os.getenv("BASE_URL", self.config.get("ENVIRONMENT", "base_url"))
    
    def get_browser(self):
        """Get browser type from config.
        
        Returns:
            str: Browser name ('chrome' or 'firefox')
        """
        return os.getenv("BROWSER", self.config.get("BROWSER", "browser_type")).lower()
    
    def is_headless(self):
        """Check if headless mode is enabled.
        
        Returns:
            bool: True if headless mode should be enabled
        """
        headless_env = os.getenv("HEADLESS", "").lower()
        if headless_env in ("true", "1", "yes"):
            return True
        
        headless_config = self.config.get("BROWSER", "headless").lower()
        return headless_config == "true"
    
    # Keep backward compatibility with existing ReadConfig.get() method
    @staticmethod
    def get(section, key):
        """Backward compatibility method for existing code.
        
        Usage:
            ReadConfig.get("TEST_DATA", "registration_first_name")
        """
        config = configparser.ConfigParser()
        config_path = Path(__file__).resolve().parent.parent / "Configurations" / "config.ini"
        config.read(config_path)
        try:
            return config.get(section, key)
        except configparser.NoSectionError:
            raise ValueError(f"Section '{section}' not found in config.ini")
        except configparser.NoOptionError:
            raise ValueError(f"Key '{key}' not found in section '{section}' of config.ini")
