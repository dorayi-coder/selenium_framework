"""BaseClass for WebDriver initialization and browser configuration.

Responsibility:
- WebDriver instantiation with browser-specific configuration
- Cross-browser support (Chrome, Firefox)
- Headless mode for CI/CD environments
- Browser options and realistic user-agent setup
- Safe WebDriver cleanup and teardown

This class is INDEPENDENT of:
- Test logic
- Page objects
- Business flows
- Assertions
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from utilities.customLogger import LoggerFactory


class BaseClass:
    """Handles WebDriver initialization and browser configuration.
    
    Supports:
    - Chrome and Firefox browsers
    - Headless mode for CI/CD pipelines
    - Realistic browser options (user-agent, window size, etc.)
    - Safe WebDriver cleanup
    """
    
    logger = LoggerFactory.get_logger(__name__)
    
    def __init__(self, browser_name="chrome", headless=False):
        """Initialize BaseClass with browser configuration.
        
        Args:
            browser_name (str): Browser to use - 'chrome' or 'firefox' (default: 'chrome')
            headless (bool): Run browser in headless mode for CI/CD (default: False)
        """
        self.browser_name = browser_name.lower()
        self.headless = headless
        self.driver = None
        
    def initialize_driver(self):
        """Initialize and return WebDriver instance.
        
        Applies browser-specific options and configurations before
        creating the WebDriver instance.
        
        Returns:
            WebDriver: Configured Selenium WebDriver instance
            
        Raises:
            ValueError: If unsupported browser is specified
        """
        self.logger.info(f"Initializing WebDriver for browser: {self.browser_name}")
        
        if self.browser_name == "chrome":
            self.driver = self._setup_chrome()
        elif self.browser_name == "firefox":
            self.driver = self._setup_firefox()
        else:
            raise ValueError(f"Unsupported browser: {self.browser_name}. "
                           "Use 'chrome' or 'firefox'")
        
        self.logger.info(f"WebDriver initialized successfully for {self.browser_name}")
        return self.driver
    
    def _setup_chrome(self):
        """Setup and return Chrome WebDriver with realistic options.
        
        Returns:
            WebDriver: Configured Chrome WebDriver instance
        """
        self.logger.info("Configuring Chrome browser options")
        
        options = ChromeOptions()
        
        # Realistic user-agent
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/118.0.5993.90 Safari/537.36"
        )
        
        # Start browser maximized
        options.add_argument("--start-maximized")
        
        # Disable automation detection
        options.add_argument("--disable-blink-features=AutomationControlled")
        
        # Window size
        options.add_argument("--window-size=1920,1080")
        
        # Disable notifications
        options.add_argument("--disable-notifications")
        
        # Disable popup blocking
        options.add_argument("--disable-popup-blocking")
        
        # Disable browser extensions
        options.add_argument("--disable-extensions")
        
        # Disable images for faster load (optional - remove if needed)
        # options.add_argument("--blink-settings=imagesEnabled=false")
        
        # Headless mode for CI/CD
        if self.headless:
            self.logger.info("Running Chrome in headless mode for CI/CD")
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        
        # Initialize Chrome WebDriver with webdriver-manager
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        
        self.logger.info("Chrome WebDriver initialized with options applied")
        return driver
    
    def _setup_firefox(self):
        """Setup and return Firefox WebDriver with realistic options.
        
        Returns:
            WebDriver: Configured Firefox WebDriver instance
        """
        self.logger.info("Configuring Firefox browser options")
        
        options = FirefoxOptions()
        
        # Realistic user-agent
        options.set_preference(
            "general.useragent.override",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) "
            "Gecko/20100101 Firefox/121.0"
        )
        
        # Window size
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        
        # Disable notifications
        options.set_preference("dom.webnotifications.enabled", False)
        
        # Headless mode for CI/CD
        if self.headless:
            self.logger.info("Running Firefox in headless mode for CI/CD")
            options.add_argument("--headless")
        
        # Initialize Firefox WebDriver with webdriver-manager
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
        
        self.logger.info("Firefox WebDriver initialized with options applied")
        return driver
    
    def quit_driver(self):
        """Safely terminate WebDriver and close browser.
        
        Should be called in test teardown or fixture cleanup.
        """
        if self.driver:
            self.logger.info(f"Quitting {self.browser_name} WebDriver")
            try:
                self.driver.quit()
                self.logger.info(f"{self.browser_name} browser closed successfully")
            except Exception as e:
                self.logger.warning(f"Error while quitting driver: {str(e)}")
            finally:
                self.driver = None
    
    def get_driver(self):
        """Get the current WebDriver instance.
        
        Returns:
            WebDriver: Current Selenium WebDriver instance or None
        """
        return self.driver
