"""
Test for LoginFlow.validate_login_using_keyboard_keys() method.

This test validates that the login flow completes successfully using only
keyboard interactions (Tab for navigation, Enter for form submission).

Test Scope: UI - Accessibility Test Case
Flow Method: LoginFlow.validate_login_using_keyboard_keys()
"""

import pytest
from flows.loginFlow import LoginFlow
from utilities.customLogger import LoggerFactory
from utilities.readProperties import ReadConfig

logger = LoggerFactory.get_logger(__name__)


@pytest.mark.ui
@pytest.mark.regression
def test_validate_login_using_keyboard_keys(driver):
    """
    Test that login succeeds when all interactions are performed using keyboard keys.
    
    Scenario: User completes login using keyboard navigation (Tab) and form submission (Enter)
    Expected Behavior:
    - Email field should accept keyboard input
    - Tab key should navigate to password field
    - Password field should accept keyboard input
    - Enter key should submit the form via keyboard
    - Login should succeed
    - Logout link should be visible after successful login
    
    Args:
        driver: WebDriver fixture providing browser instance
    
    Assertions:
    - Login should succeed with keyboard interaction
    - Keyboard navigation should complete successfully
    - User should be logged in (logout link visible)
    """
    logger.info("="*80)
    logger.info("Starting test: validate_login_using_keyboard_keys")
    logger.info("="*80)
    
    # Initialize LoginFlow with WebDriver
    login_flow = LoginFlow(driver)
    
    # Test data - valid login credentials
    email = ReadConfig.get("LOGIN", "email")
    password = ReadConfig.get("LOGIN", "password")
    
    logger.info(f"Attempting login using keyboard keys - email: {email}")
    
    # Execute the flow method under test
    result = login_flow.validate_login_using_keyboard_keys(email, password)
    
    logger.info(f"Flow returned result: {result}")
    
    # ===== Assertions =====
    
    print("\n" + "="*80)
    print("TEST RESULT:")
    print("="*80)
    print(f"Login Success: {result['success']}")
    print(f"Keyboard Navigation Success: {result['keyboard_navigation_success']}")
    print(f"Has Any Error: {result['has_any_error']}")
    print(f"Error Message: {result['error_message']}")
    print(f"Validation Errors: {result['validation_errors']}")
    print("="*80 + "\n")
    
    # Assertion 1: Keyboard navigation should complete successfully
    assert result['keyboard_navigation_success'] is True, \
        f"Assertion 1: Expected keyboard navigation to succeed, but keyboard_navigation_success={result['keyboard_navigation_success']}"
    
    # Assertion 2: Login should succeed with keyboard interaction
    assert result['success'] is True, \
        f"Assertion 2: Expected login to succeed with keyboard keys, but login succeeded={result['success']}"
    
    # Assertion 3: No error state should be present
    assert result['has_any_error'] is False, \
        f"Assertion 3: Expected no errors with keyboard login, but has_any_error={result['has_any_error']}"
    
    logger.info("="*80)
    logger.info("Test PASSED: validate_login_using_keyboard_keys")
    logger.info("="*80)
