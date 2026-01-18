"""Pytest test for user registration with mandatory fields only.

Tests the RegisterFlow.register_with_mandatory_fields() method.
Verifies that a user can successfully register using only mandatory fields.

Test Layer Only:
- Imports Flow classes (no Page objects)
- Calls ONE Flow method only
- Verifies business outcomes via assertions
- No locators, waits, sleeps, or Selenium APIs
- No browser setup/teardown (handled by fixtures)
- Uses configuration from Configurations/config.ini
"""

import pytest
from flows.registerFlow import RegisterFlow
from utilities.customLogger import LoggerFactory
from utilities.readProperties import ReadConfig
import uuid

logger = LoggerFactory.get_logger(__name__)


@pytest.mark.ui
@pytest.mark.regression
def test_user_registers_successfully_with_mandatory_fields(driver):
    """
    Test: User registration with mandatory fields only.

    Flow Method: RegisterFlow.register_with_mandatory_fields()

    Precondition: User is on the registration page

    Steps:
    1. Load registration test data from config.ini
    2. Initialize RegisterFlow with driver
    3. Call register_with_mandatory_fields() with valid mandatory data from config
    4. Verify registration success

    Expected Result: User successfully registers and is redirected to account page
    or success message is displayed, indicating registration completed.

    Postcondition: User account is created and user is authenticated
    """
    logger.info("Starting test: User registration with mandatory fields")

    # Load test data from config.ini [TEST_DATA] section
    first_name = ReadConfig.get("TEST_DATA", "registration_first_name")
    last_name = ReadConfig.get("TEST_DATA", "registration_last_name")
    password = ReadConfig.get("TEST_DATA", "registration_password")

    # Generate unique email using UUID to avoid conflicts
    unique_email = f"user.{uuid.uuid4().hex[:8]}@example.com"

    logger.info(f"Using test data from config.ini: first_name={first_name}, last_name={last_name}")
    logger.info(f"Generated unique email: {unique_email}")

    # Initialize the Flow
    register_flow = RegisterFlow(driver)

    # Call the Flow method with mandatory fields only
    # Mandatory fields: First Name, Last Name, Email, Password
    success = register_flow.register_with_mandatory_fields(
        first_name=first_name,
        last_name=last_name,
        email=unique_email,
        password=password
    )

    # Verify registration success
    logger.info("Verifying registration success")
    assert success is True, "Registration flow should return True on success"

    # Verify user is authenticated (on dashboard/account page)
    is_logged_in = register_flow.is_user_logged_in()
    assert is_logged_in is True, "User should be logged in after registration"

    logger.info("✓ Test passed: User successfully registered with mandatory fields")


@pytest.mark.ui
@pytest.mark.regression
def test_user_registration_with_valid_mandatory_data(driver):
    """
    Alternative test case: Registration with different valid data.

    Tests the same Flow method with alternative valid data loaded from config.ini.
    Verifies that the Flow can handle multiple valid input scenarios.
    """
    logger.info("Starting test: User registration with alternative data from config")

    # Load alternative test data from config.ini [TEST_DATA] section
    first_name = ReadConfig.get("TEST_DATA", "registration_first_name_alt")
    last_name = ReadConfig.get("TEST_DATA", "registration_last_name_alt")
    password = ReadConfig.get("TEST_DATA", "registration_password_alt")

    # Generate unique email using UUID to avoid conflicts
    unique_email = f"user.{uuid.uuid4().hex[:8]}@example.com"

    logger.info(f"Using alternative test data from config.ini: first_name={first_name}, last_name={last_name}")
    logger.info(f"Generated unique email: {unique_email}")

    # Initialize the Flow
    register_flow = RegisterFlow(driver)

    # Call the Flow method with alternative valid mandatory data
    success = register_flow.register_with_mandatory_fields(
        first_name=first_name,
        last_name=last_name,
        email=unique_email,
        password=password
    )

    # Verify registration success
    logger.info("Verifying registration success with alternative data")
    assert success is True, "Registration should succeed with valid alternative data from config"

    # Verify user can access their account
    is_logged_in = register_flow.is_user_logged_in()
    assert is_logged_in is True, "User should be authenticated after registration"

    # Additional verification: Check if account dashboard is accessible
    dashboard_visible = register_flow.is_account_dashboard_visible()
    assert dashboard_visible is True, "User account dashboard should be visible after registration"

    logger.info("✓ Test passed: User registration with alternative data successful")
