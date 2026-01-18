"""BaseTest with Pytest fixtures for WebDriver lifecycle management.

Responsibility:
- Pytest fixture providing WebDriver to test functions
- Reading browser selection from pytest CLI option (--browser)
- Initializing WebDriver via BaseClass
- Ensuring proper driver cleanup after each test
- Supporting cross-browser test execution

This class is INDEPENDENT of:
- Page objects
- Business flows
- Test logic
- Assertions
"""

import pytest
from base.base_class import BaseClass
from utilities.customLogger import LoggerFactory
from utilities.session_manager import SessionManager
from utilities.readProperties import ReadConfig


logger = LoggerFactory.get_logger(__name__)


def pytest_addoption(parser):
    """Add custom pytest command-line options.
    
    Allows users to specify browser and headless mode:
    - pytest --browser=chrome
    - pytest --browser=firefox
    - pytest --headless
    """
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to use for tests: chrome or firefox (default: chrome)"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run tests in headless mode for CI/CD environments"
    )


@pytest.fixture(scope="function")
def driver(request):
    """Pytest fixture providing WebDriver instance with session cookie reuse.
    
    Scope: function - Fresh WebDriver for each test
    
    Features:
    - Reads browser from --browser CLI option
    - Supports headless mode via --headless flag
    - Attempts to reuse session cookies to avoid repeated Cloudflare challenges
    - Falls back gracefully to fresh session if cookies unavailable
    - Initializes WebDriver via BaseClass
    - Saves session cookies for future reuse (reduces Cloudflare friction)
    - Ensures driver cleanup after test execution
    - Logs driver initialization and teardown
    
    Session Cookie Strategy:
    1. Initialize fresh WebDriver
    2. If valid cookies exist, load them
    3. If cookies loaded, refresh browser to activate session
    4. If no cookies or load failed, let test open page normally
    5. After test, save cookies for next run
    
    This approach:
    - Reduces Cloudflare Turnstile challenges (not bypassing, just reusing)
    - Improves test execution speed
    - Gracefully handles missing/stale cookies
    - Works locally and in CI/CD (GitLab)
    
    Usage in tests:
        def test_something(driver):
            driver.get("https://example.com")
            # Test logic here
            # driver cleanup and cookie save happens automatically
    
    Args:
        request: Pytest request fixture for accessing CLI options
        
    Yields:
        WebDriver: Initialized Selenium WebDriver instance
    """
    # Read browser and headless options from CLI
    browser_name = request.config.getoption("--browser")
    headless_mode = request.config.getoption("--headless")
    
    logger.info("=" * 70)
    logger.info(f"Test: {request.node.name}")
    logger.info(f"Browser: {browser_name} | Headless: {headless_mode}")
    logger.info("=" * 70)
    
    # Initialize BaseClass and WebDriver
    base_class = BaseClass(browser_name=browser_name, headless=headless_mode)
    driver_instance = base_class.initialize_driver()
    
    # ===== SESSION COOKIE REUSE =====
    session_mgr = SessionManager(driver=driver_instance)
    cookies_reused = False
    
    try:
        # Step 1: Check if valid cookies exist
        if session_mgr.cookies_exist():
            logger.info("Valid session cookies found - attempting to reuse")
            
            # Step 2: Load cookies into driver
            if session_mgr.load_cookies(driver_instance):
                # Step 3: Navigate to base URL to activate loaded session
                base_url = ReadConfig.get("APPLICATION", "base_url")
                logger.info(f"Refreshing session by navigating to {base_url}")
                driver_instance.get(base_url)
                
                logger.info("Session reused successfully - Cloudflare should be bypassed")
                cookies_reused = True
            else:
                logger.info("Failed to load cookies - proceeding with fresh session")
        else:
            logger.info("No valid session cookies available - fresh session will be created")
    
    except Exception as e:
        logger.warning(f"Session cookie reuse failed gracefully: {str(e)}")
        logger.info("Proceeding with fresh session for this test")
    
    logger.info(f"Driver ready for test (cookies_reused={cookies_reused})")
    
    # Yield driver to test
    yield driver_instance
    
    # ===== SAVE SESSION COOKIES FOR NEXT TEST =====
    try:
        logger.info("Attempting to save session cookies for future tests")
        session_mgr.save_cookies(driver_instance)
    except Exception as e:
        logger.warning(f"Could not save session cookies: {str(e)}")
    
    # Cleanup - always executed after test
    logger.info("-" * 70)
    logger.info(f"Test completed: {request.node.name}")
    logger.info("Cleaning up WebDriver...")
    base_class.quit_driver()
    logger.info("-" * 70)


# Optional: Fixture for test result tracking
@pytest.fixture(scope="function")
def test_result(request):
    """Optional fixture to track test pass/fail status.
    
    Usage:
        def test_something(driver, test_result):
            test_result["passed"] = True  # or False
    """
    result = {"passed": False}
    yield result
    
    status = "PASSED" if result["passed"] else "FAILED"
    logger.info(f"Test Result: {request.node.name} - {status}")
