"""
Test for LoginFlow.validate_login_with_invalid_email() method.

This test validates that the login flow properly handles invalid email addresses.

Test Scope: UI - Negative Test Case
Flow Method: LoginFlow.validate_login_with_invalid_email()
"""

import pytest
from flows.loginFlow import LoginFlow
from utilities.customLogger import LoggerFactory

logger = LoggerFactory.get_logger(__name__)


@pytest.mark.ui
@pytest.mark.negative
@pytest.mark.regression
def test_validate_login_with_invalid_email(driver):
    """
    Test that login fails appropriately when an invalid email format is provided.
    
    Scenario: User attempts to login with an invalid/malformed email address
    Expected Behavior:
    - Login should NOT succeed (logout link not visible)
    - Error state should be present
    
    Args:
        driver: WebDriver fixture providing browser instance
    
    Assertions:
    - Login should fail (success=False)
    - Error state should be detected
    """
    logger.info("="*80)
    logger.info("Starting test: validate_login_with_invalid_email")
    logger.info("="*80)
    
    # Initialize LoginFlow with WebDriver
    login_flow = LoginFlow(driver)
    
    # Test data - invalid email formats
    invalid_email = "notanemail"  # Missing @ and domain
    password = "TestPassword123"  # Password can be valid
    
    logger.info(f"Attempting login with invalid email: '{invalid_email}'")
    
    # Execute the flow method under test
    result = login_flow.validate_login_with_invalid_email(invalid_email, password)
    
    logger.info(f"Flow returned result: {result}")
    
    # ===== Assertions =====
    
    print("\n" + "="*80)
    print("TEST RESULT:")
    print("="*80)
    print(f"Login Success: {result['success']}")
    print(f"Has Any Error: {result['has_any_error']}")
    print(f"Error Message: {result['error_message']}")
    print(f"Validation Errors: {result['validation_errors']}")
    print("="*80 + "\n")
    
    # Assertion 1: Login should NOT succeed with invalid email
    if result['success'] is True:
        print("This is an invalid email")
        logger.error("Login succeeded with invalid email - This should not happen!")
    
    assert result['success'] is False, \
        f"Assertion 1: Expected login to fail with invalid email, but login succeeded"
    
    # Assertion 2: At least one error state should be present
    assert result['has_any_error'] is True, \
        f"Expected error state to be present, but no errors detected"
    
    logger.info("="*80)
    logger.info("Test PASSED: validate_login_with_invalid_email")
    logger.info("="*80)
