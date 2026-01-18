"""Stable WebDriver factory for reliable automated testing.

Implements SDET-level approach:
- Reliable Chrome WebDriver setup
- Proper error handling and logging
- Focus on stability and test reliability
- No evasion tactics - standard browser configuration
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utilities.customLogger import LoggerFactory

logger = LoggerFactory.get_logger(__name__)


class StableWebDriver:
    """Stable and reliable WebDriver manager for SDET testing."""
    
    @staticmethod
    def create_driver():
        """Create standard Chrome WebDriver with proper configuration.
        
        Returns:
            WebDriver: Configured Chrome WebDriver instance
        """
        logger.info("Creating Chrome WebDriver")
        
        try:
            from webdriver_manager.chrome import ChromeDriverManager
            from selenium.webdriver.chrome.service import Service
        except ImportError:
            logger.warning("webdriver_manager not installed, using system chromedriver")
            from selenium.webdriver.chrome.service import Service
            Service = None
        
        options = webdriver.ChromeOptions()
        
        # Check if headless mode is enabled
        import os
        headless = os.getenv("HEADLESS", "false").lower() == "true"
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
        
        # Standard browser options for stability and compatibility
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-popup-blocking")
        
        try:
            if Service:
                try:
                    service = Service(ChromeDriverManager().install())
                    driver = webdriver.Chrome(service=service, options=options)
                    logger.info("WebDriver created with webdriver_manager")
                except Exception as e:
                    logger.warning(f"webdriver_manager failed ({str(e)}), using system chromedriver")
                    driver = webdriver.Chrome(options=options)
            else:
                driver = webdriver.Chrome(options=options)
            
            # Configure timeouts
            driver.implicitly_wait(10)
            driver.set_page_load_timeout(60)
            
            logger.info("Chrome WebDriver initialized successfully")
            return driver
            
        except Exception as e:
            logger.error(f"Failed to create Chrome WebDriver: {str(e)}")
            raise
    



class StandardChromeDriver:
    """Legacy compatibility - use StableWebDriver instead."""
    
    @staticmethod
    def create_driver():
        """Create standard Chrome WebDriver (delegates to StableWebDriver)."""
        return StableWebDriver.create_driver()


__all__ = ['StableWebDriver', 'StandardChromeDriver']
