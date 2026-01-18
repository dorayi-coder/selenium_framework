"""Pytest configuration and fixtures for test suite.

Provides fixtures for:
- Login flow orchestration
- Downloads flow orchestration
- Page object instances
- Session management
- Cleanup and teardown
"""

import pytest
from utilities.customLogger import LoggerFactory
from utilities.readProperties import ReadConfig

logger = LoggerFactory.get_logger(__name__)


@pytest.fixture(scope="function")
def driver():
    """
    Fixture providing WebDriver instance.
    
    Scope: Function
    - Creates fresh browser instance for each test
    - Manages browser lifecycle with proper cleanup
    - Uses explicit waits for element interactions
    
    Features:
    - Professional Chrome WebDriver setup
    - Reasonable window size and standard options
    - Proper browser lifecycle management
    """
    logger.info("Setting up WebDriver fixture")
    
    from utilities.antiDetectionDriver import StableWebDriver
    driver = StableWebDriver.create_driver()
    
    # Navigate to base URL
    base_url = ReadConfig.get("APPLICATION", "base_url")
    logger.info(f"Navigating to base URL: {base_url}")
    driver.get(base_url)
    
    logger.info("WebDriver fixture ready for test")
    
    yield driver
    
    logger.info("Tearing down WebDriver fixture")
    driver.quit()


@pytest.fixture(scope="function")
def login_page():
    """
    Fixture providing LoginPage object instance.
    
    Scope: Function
    - Fresh page object for each test
    - Ensures clean state between tests
    """
    logger.info("Setting up LoginPage fixture")
    from pages.login_page import LoginPage
    
    page = LoginPage()
    page.navigate_to_login()
    
    yield page
    
    logger.info("Tearing down LoginPage fixture")


@pytest.fixture(scope="function")
def login_flow(login_page):
    """
    Fixture providing LoginFlow orchestration.
    
    Scope: Function
    - Uses login_page fixture as dependency
    - Provides business-level login operations
    """
    logger.info("Setting up LoginFlow fixture")
    from flows.login_flow import LoginFlow
    
    flow = LoginFlow(login_page)
    
    yield flow
    
    logger.info("Tearing down LoginFlow fixture")
    if flow.is_user_logged_in():
        flow.logout()


@pytest.fixture(scope="function")
def password_reset_flow():
    """
    Fixture providing PasswordResetFlow orchestration.
    
    Scope: Function
    - Provides password reset operations
    """
    logger.info("Setting up PasswordResetFlow fixture")
    from flows.password_reset_flow import PasswordResetFlow
    from pages.password_reset_page import PasswordResetPage
    
    page = PasswordResetPage()
    flow = PasswordResetFlow(page)
    
    yield flow
    
    logger.info("Tearing down PasswordResetFlow fixture")


@pytest.fixture(scope="function")
def account_recovery_flow():
    """
    Fixture providing AccountRecoveryFlow orchestration.
    
    Scope: Function
    - Provides account unlock operations
    """
    logger.info("Setting up AccountRecoveryFlow fixture")
    from flows.account_recovery_flow import AccountRecoveryFlow
    
    flow = AccountRecoveryFlow()
    
    yield flow
    
    logger.info("Tearing down AccountRecoveryFlow fixture")


@pytest.fixture(scope="function")
def downloads_page():
    """
    Fixture providing DownloadsPage object instance.
    
    Scope: Function
    - Fresh page object for each test
    - Ensures clean state between tests
    """
    logger.info("Setting up DownloadsPage fixture")
    from pages.downloads_page import DownloadsPage
    
    page = DownloadsPage()
    page.navigate_to_downloads()
    
    yield page
    
    logger.info("Tearing down DownloadsPage fixture")


@pytest.fixture(scope="function")
def downloads_flow(downloads_page):
    """
    Fixture providing DownloadsFlow orchestration.
    
    Scope: Function
    - Uses downloads_page fixture as dependency
    - Provides business-level download operations
    """
    logger.info("Setting up DownloadsFlow fixture")
    from flows.downloads_flow import DownloadsFlow
    
    flow = DownloadsFlow(downloads_page)
    
    yield flow
    
    logger.info("Tearing down DownloadsFlow fixture")
    flow.cleanup_downloads()


@pytest.fixture(scope="function")
def transactions_page():
    """
    Fixture providing TransactionsPage object instance.
    
    Scope: Function
    - Fresh page object for each test
    - Ensures clean state between tests
    """
    logger.info("Setting up TransactionsPage fixture")
    from pages.transactions_page import TransactionsPage
    
    page = TransactionsPage()
    page.navigate_to_transactions()
    
    yield page
    
    logger.info("Tearing down TransactionsPage fixture")


@pytest.fixture(scope="function")
def transactions_flow(transactions_page):
    """
    Fixture providing TransactionsFlow orchestration.
    
    Scope: Function
    - Uses transactions_page fixture as dependency
    - Provides business-level transaction operations
    """
    logger.info("Setting up TransactionsFlow fixture")
    from flows.transactions_flow import TransactionsFlow
    
    flow = TransactionsFlow(transactions_page)
    
    yield flow
    
    logger.info("Tearing down TransactionsFlow fixture")
    flow.cleanup_transactions()


@pytest.fixture(scope="function")
def recurring_payments_page():
    """
    Fixture providing RecurringPaymentsPage object instance.
    
    Scope: Function
    - Fresh page object for each test
    - Ensures clean state between tests
    """
    logger.info("Setting up RecurringPaymentsPage fixture")
    from pages.recurring_payments_page import RecurringPaymentsPage
    
    page = RecurringPaymentsPage()
    page.navigate_to_recurring_payments()
    
    yield page
    
    logger.info("Tearing down RecurringPaymentsPage fixture")


@pytest.fixture(scope="function")
def recurring_payments_flow(recurring_payments_page):
    """
    Fixture providing RecurringPaymentsFlow orchestration.
    
    Scope: Function
    - Uses recurring_payments_page fixture as dependency
    - Provides business-level recurring payment operations
    """
    logger.info("Setting up RecurringPaymentsFlow fixture")
    from flows.recurring_payments_flow import RecurringPaymentsFlow
    
    flow = RecurringPaymentsFlow(recurring_payments_page)
    
    yield flow
    
    logger.info("Tearing down RecurringPaymentsFlow fixture")


@pytest.fixture(autouse=True)
def log_test_info(request):
    """
    Autouse fixture to log test start and end.
    
    Automatically runs for every test without explicit request.
    """
    logger.info(f"{'='*60}")
    logger.info(f"Starting test: {request.node.name}")
    logger.info(f"{'='*60}")
    
    yield
    
    logger.info(f"{'='*60}")
    logger.info(f"Completed test: {request.node.name}")
    logger.info(f"{'='*60}")


@pytest.fixture(scope="session", autouse=True)
def session_setup_teardown():
    """
    Session-scoped fixture for one-time setup/teardown.
    
    Runs once per test session.
    """
    logger.info("Session started: Initializing test environment")
    
    yield
    
    logger.info("Session ended: Cleaning up test environment")


@pytest.fixture
def clean_browser_state(login_flow):
    """
    Fixture ensuring clean browser state before test.
    
    - Clears cookies
    - Clears localStorage
    - Clears sessionStorage
    """
    logger.info("Clearing browser state")
    login_flow.clear_cookies()
    login_flow.clear_local_storage()
    login_flow.clear_session_storage()
    
    yield
    
    logger.info("Cleaning up browser state after test")
    login_flow.clear_cookies()


@pytest.fixture
def authenticated_user_session(login_flow):
    """
    Fixture providing pre-authenticated user session.
    
    Use this fixture when test requires user to already be logged in.
    """
    from testdata.login_testdata import VALID_CREDENTIALS
    
    logger.info("Setting up authenticated user session")
    
    login_flow.perform_login(
        email=VALID_CREDENTIALS["email"],
        password=VALID_CREDENTIALS["password"],
    )
    
    yield login_flow
    
    logger.info("Tearing down authenticated user session")
    if login_flow.is_user_logged_in():
        login_flow.logout()


@pytest.fixture
def capture_screenshot_on_failure(request):
    """
    Fixture to capture screenshot on test failure.
    
    Automatically captures screenshot when test fails.
    """
    yield
    
    if request.node.rep_call.failed:
        logger.error(f"Test failed: {request.node.name}")


def pytest_configure(config):
    """
    Pytest hook for initial configuration.
    
    Registers custom markers and initializes framework.
    """
    config.addinivalue_line(
        "markers", "smoke: mark test as smoke test"
    )
    config.addinivalue_line(
        "markers", "regression: mark test as regression test"
    )
    config.addinivalue_line(
        "markers", "security: mark test as security test"
    )
    config.addinivalue_line(
        "markers", "performance: mark test as performance test"
    )


@pytest.fixture(scope="function")
def affiliate_page():
    """
    Fixture providing AffiliatePage object instance.
    
    Scope: Function
    - Fresh page object for each test
    - Ensures clean state between tests
    """
    logger.info("Setting up AffiliatePage fixture")
    from pages.affiliatePage import AffiliatePage
    
    page = AffiliatePage()
    
    yield page
    
    logger.info("Tearing down AffiliatePage fixture")


@pytest.fixture(scope="function")
def affiliate_flow(affiliate_page):
    """
    Fixture providing AffiliateFlow orchestration.
    
    Scope: Function
    - Uses affiliate_page fixture as dependency
    - Provides business-level affiliate operations
    """
    logger.info("Setting up AffiliateFlow fixture")
    from flows.affiliateFlow import AffiliateFlow
    
    flow = AffiliateFlow(affiliate_page.driver)
    
    yield flow
    
    logger.info("Tearing down AffiliateFlow fixture")


@pytest.fixture(scope="function")
def newsletter_page():
    """
    Fixture providing NewsletterPage object instance.
    
    Scope: Function
    - Fresh page object for each test
    - Ensures clean state between tests
    """
    logger.info("Setting up NewsletterPage fixture")
    from pages.newsletterPage import NewsletterPage
    
    page = NewsletterPage()
    
    yield page
    
    logger.info("Tearing down NewsletterPage fixture")


@pytest.fixture(scope="function")
def newsletter_flow(newsletter_page):
    """
    Fixture providing NewsletterFlow orchestration.
    
    Scope: Function
    - Uses newsletter_page fixture as dependency
    - Provides business-level newsletter operations
    """
    logger.info("Setting up NewsletterFlow fixture")
    from flows.newsletterFlow import NewsletterFlow
    
    flow = NewsletterFlow(newsletter_page.driver)
    
    yield flow
    
    logger.info("Tearing down NewsletterFlow fixture")


@pytest.fixture(scope="function")
def register_page():
    """
    Fixture providing RegisterPage object instance.
    
    Scope: Function
    - Fresh page object for each test
    - Ensures clean state between tests
    """
    logger.info("Setting up RegisterPage fixture")
    from pages.registerPage import RegisterPage
    
    page = RegisterPage(None)
    
    yield page
    
    logger.info("Tearing down RegisterPage fixture")


@pytest.fixture(scope="function")
def register_flow(driver):
    """
    Fixture providing RegisterFlow orchestration.
    
    Scope: Function
    - Uses driver fixture as dependency
    - Provides business-level registration operations
    """
    logger.info("Setting up RegisterFlow fixture")
    from flows.registerFlow import RegisterFlow
    
    flow = RegisterFlow(driver)
    
    yield flow
    
    logger.info("Tearing down RegisterFlow fixture")


def pytest_runtest_makereport(item, call):
    """
    Pytest hook to capture test result information.
    
    Allows fixtures to access test result data.
    """
    if call.when == "call":
        item.rep_call = call
