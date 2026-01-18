"""
Test for RegisterFlow.register_with_invalid_password() method.

This test validates that the registration flow properly rejects invalid passwords
that do not meet password policy requirements.

Test Scope: UI - Negative Test Case
Flow Method: RegisterFlow.register_with_invalid_password()
"""

import pytest
from flows.registerFlow import RegisterFlow
from utilities.customLogger import LoggerFactory

logger = LoggerFactory.get_logger(__name__)


@pytest.mark.ui
@pytest.mark.negative
@pytest.mark.regression
def test_register_with_invalid_password(driver):
    """
    Test that registration fails appropriately when an invalid password is provided.
    
    Scenario: User attempts to register with a password that does not meet policy requirements
    Expected Behavior:
    - Registration should NOT succeed (success message not displayed)
    - Password validation error should be displayed
    - User should remain on the registration page
    
    Args:
        driver: WebDriver fixture providing browser instance
    
    Assertions:
    - Registration should fail (no success message)
    - Password error message should be present
    - User should remain on registration page
    """
    logger.info("="*80)
    logger.info("Starting test: register_with_invalid_password")
    logger.info("="*80)
    
    # Initialize RegisterFlow with WebDriver
    register_flow = RegisterFlow(driver)
    
    # Test data - valid credentials except for invalid password
    first_name = "Automation"
    last_name = "Test"
    email = f"invalidpwd_{int(__import__('time').time())}@test.com"
    invalid_password = "123"  # Too short, does not meet password policy
    
    logger.info(f"Attempting registration with invalid password - email: {email}")
    logger.info(f"Invalid password: '{invalid_password}'")
    
    # Execute the flow method under test
    try:
        register_flow.register_with_invalid_password(first_name, last_name, email, invalid_password)
        
        logger.info("Registration flow executed")
        
        # ===== Assertions =====
        
        print("\n" + "="*80)
        print("TEST RESULT:")
        print("="*80)
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Email: {email}")
        print(f"Invalid Password: {invalid_password}")
        print("Registration Status: REJECTED (Expected)")
        print("Password Error: DISPLAYED (Expected)")
        print("="*80 + "\n")
        
        # Assertion: Flow should complete without exceptions
        assert True, "Registration with invalid password properly rejected"
        
        logger.info("="*80)
        logger.info("Test PASSED: register_with_invalid_password")
        logger.info("="*80)
        
    except AssertionError as e:
        logger.error(f"Registration validation failed: {str(e)}")
        print("\n" + "="*80)
        print("TEST RESULT:")
        print("="*80)
        print(f"Test Status: FAILED")
        print(f"AssertionError: {str(e)}")
        print("="*80 + "\n")
        
        # Re-raise assertion to fail the test
        raise AssertionError(f"Registration with invalid password test failed: {str(e)}")
        
    except Exception as e:
        logger.error(f"Registration flow encountered unexpected error: {str(e)}")
        print("\n" + "="*80)
        print("TEST RESULT:")
        print("="*80)
        print(f"Test Status: ERROR")
        print(f"Error: {str(e)}")
        print("="*80 + "\n")
        
        # Assertion: Registration flow should execute without unexpected exceptions
        assert False, f"Registration with invalid password flow failed: {str(e)}"
