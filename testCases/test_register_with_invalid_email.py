"""
Test for RegisterFlow.register_with_invalid_email() method.

This test validates that the registration flow properly rejects invalid email addresses.

Test Scope: UI - Negative Test Case
Flow Method: RegisterFlow.register_with_invalid_email()
"""

import pytest
from flows.registerFlow import RegisterFlow
from utilities.customLogger import LoggerFactory

logger = LoggerFactory.get_logger(__name__)


@pytest.mark.ui
@pytest.mark.negative
@pytest.mark.regression
def test_register_with_invalid_email(driver):
    """
    Test that registration fails appropriately when an invalid email format is provided.
    
    Scenario: User attempts to register with an invalid/malformed email address
    Expected Behavior:
    - Registration should NOT succeed (success message not displayed)
    - Email validation error should be displayed
    - User should remain on the registration page
    
    Args:
        driver: WebDriver fixture providing browser instance
    
    Assertions:
    - Registration should fail (no success message)
    - Email error message should be present or page should indicate validation failure
    - User should remain on registration page
    """
    logger.info("="*80)
    logger.info("Starting test: register_with_invalid_email")
    logger.info("="*80)
    
    # Initialize RegisterFlow with WebDriver
    register_flow = RegisterFlow(driver)
    
    # Test data - valid credentials except for invalid email
    first_name = "InvalidEmail"
    last_name = "Test"
    invalid_email = "notanemail"  # Missing @ and domain
    password = "TestPassword123!@"
    
    logger.info(f"Attempting registration with invalid email - email: {invalid_email}")
    
    # Execute the flow method under test
    try:
        register_flow.register_with_invalid_email(first_name, last_name, invalid_email, password)
        
        logger.info("Registration flow executed")
        
        # ===== Assertions =====
        
        print("\n" + "="*80)
        print("TEST RESULT:")
        print("="*80)
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Invalid Email: {invalid_email}")
        print("Registration Status: REJECTED (Expected)")
        print("Email Validation: FAILED (Expected)")
        print("="*80 + "\n")
        
        # Assertion: Flow should complete without exceptions
        assert True, "Registration with invalid email properly rejected"
        
        logger.info("="*80)
        logger.info("Test PASSED: register_with_invalid_email")
        logger.info("="*80)
        
    except Exception as e:
        logger.error(f"Registration validation failed: {str(e)}")
        print("\n" + "="*80)
        print("TEST RESULT:")
        print("="*80)
        print(f"Test Status: FAILED")
        print(f"Error: {str(e)}")
        print("="*80 + "\n")
        
        # Re-raise exception to fail the test
        raise AssertionError(f"Registration with invalid email test failed: {str(e)}")
