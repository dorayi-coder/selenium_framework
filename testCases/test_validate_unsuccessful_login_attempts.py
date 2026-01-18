"""
Test for LoginFlow.validate_unsuccessful_login_attempts() method.

This test validates that the login flow properly handles multiple unsuccessful login
attempts and tracks error states appropriately.

Test Scope: UI - Security Test Case
Flow Method: LoginFlow.validate_unsuccessful_login_attempts()
"""

import pytest
from flows.loginFlow import LoginFlow
from utilities.customLogger import LoggerFactory
from utilities.readProperties import ReadConfig

logger = LoggerFactory.get_logger(__name__)


@pytest.mark.ui
@pytest.mark.regression
def test_validate_unsuccessful_login_attempts(driver):
    """
    Test that multiple unsuccessful login attempts are properly tracked and handled.
    
    Scenario: User attempts to login multiple times with invalid credentials
    Expected Behavior:
    - All login attempts should fail (no logout link visible)
    - Error messages should be displayed for each failed attempt
    - System should track the number of failed attempts
    - User should remain on login page after all failed attempts
    - Potential account lockout or rate limiting may be detected
    
    Args:
        driver: WebDriver fixture providing browser instance
    
    Assertions:
    - All login attempts should fail
    - Failed attempts count should match total attempts
    - Error messages should be captured
    - User should not be logged in after failed attempts
    """
    logger.info("="*80)
    logger.info("Starting test: validate_unsuccessful_login_attempts")
    logger.info("="*80)
    
    # Initialize LoginFlow with WebDriver
    login_flow = LoginFlow(driver)
    
    # Test data - valid email with incorrect password
    email = ReadConfig.get("LOGIN", "email")
    invalid_password = "WrongPassword12345!@"
    num_attempts = 3
    
    logger.info(f"Attempting login {num_attempts} times with invalid credentials - email: {email}")
    
    # Execute the flow method under test
    result = login_flow.validate_unsuccessful_login_attempts(email, invalid_password, num_attempts)
    
    logger.info(f"Flow returned result: {result}")
    
    # ===== Assertions =====
    
    print("\n" + "="*80)
    print("TEST RESULT:")
    print("="*80)
    print(f"Total Attempts: {result['total_attempts']}")
    print(f"Failed Attempts: {result['failed_attempts']}")
    print(f"Login Success: {result['success']}")
    print(f"All Attempts Failed: {result['all_attempts_failed']}")
    print(f"First Error Message: {result['first_error_message']}")
    print(f"Last Error Message: {result['last_error_message']}")
    print(f"Unique Error Messages: {len(result['error_messages'])}")
    print(f"Account Lockout Detected: {result['has_account_lockout_message']}")
    print("="*80 + "\n")
    
    # Assertion 1: Total attempts should match configured attempts
    assert result['total_attempts'] == num_attempts, \
        f"Assertion 1: Expected {num_attempts} total attempts, but got {result['total_attempts']}"
    
    # Assertion 2: All attempts should have failed
    assert result['all_attempts_failed'] is True, \
        f"Assertion 2: Expected all attempts to fail, but all_attempts_failed={result['all_attempts_failed']}"
    
    # Assertion 3: Failed attempts should equal total attempts
    assert result['failed_attempts'] == num_attempts, \
        f"Assertion 3: Expected {num_attempts} failed attempts, but got {result['failed_attempts']}"
    
    # Assertion 4: Login should not succeed after failed attempts
    assert result['success'] is False, \
        f"Assertion 4: Expected login to fail with invalid credentials, but success={result['success']}"
    
    # Assertion 5: At least one error message should be captured
    assert len(result['error_messages']) > 0, \
        f"Assertion 5: Expected error messages to be captured, but got {len(result['error_messages'])}"
    
    logger.info("="*80)
    logger.info("Test PASSED: validate_unsuccessful_login_attempts")
    logger.info("="*80)
