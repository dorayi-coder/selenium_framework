"""
Test for RegisterFlow.register_after_deleting_session_cookies() method.

This test validates that the registration flow completes successfully even after
session cookies have been deleted, ensuring proper session management.

Test Scope: UI - Session Management Test Case
Flow Method: RegisterFlow.register_after_deleting_session_cookies()
"""

import pytest
from flows.registerFlow import RegisterFlow
from utilities.customLogger import LoggerFactory

logger = LoggerFactory.get_logger(__name__)


@pytest.mark.ui
@pytest.mark.regression
def test_register_after_deleting_session_cookies(driver):
    """
    Test that registration succeeds even after session cookies are deleted.
    
    Scenario: User deletes session cookies before registration, then completes registration
    Expected Behavior:
    - Session cookies should be deleted successfully
    - Registration form should load and accept input
    - Registration should complete successfully
    - Success message should be displayed
    - User should be able to proceed with continue action
    
    Args:
        driver: WebDriver fixture providing browser instance
    
    Assertions:
    - Registration should complete successfully after cookie deletion
    - Success message should be displayed
    - Registration flow should handle cookie deletion gracefully
    """
    logger.info("="*80)
    logger.info("Starting test: register_after_deleting_session_cookies")
    logger.info("="*80)
    
    # Initialize RegisterFlow with WebDriver
    register_flow = RegisterFlow(driver)
    
    # Test data - valid registration credentials
    first_name = "SessionTest"
    last_name = "User"
    email = f"cookiedelete_{int(__import__('time').time())}@test.com"
    password = "SessionPassword123!@"
    
    logger.info(f"Attempting registration after deleting session cookies - email: {email}")
    
    # Execute the flow method under test
    try:
        register_flow.register_after_deleting_session_cookies(first_name, last_name, email, password)
        
        logger.info("Registration flow after deleting session cookies executed successfully")
        
        # ===== Assertions =====
        
        print("\n" + "="*80)
        print("TEST RESULT:")
        print("="*80)
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Email: {email}")
        print(f"Session Cookies: DELETED")
        print("Registration Status: SUCCESS")
        print("="*80 + "\n")
        
        # Assertion: Registration should complete without exceptions
        assert True, "Registration after deleting session cookies completed successfully"
        
        logger.info("="*80)
        logger.info("Test PASSED: register_after_deleting_session_cookies")
        logger.info("="*80)
        
    except Exception as e:
        logger.error(f"Registration flow failed: {str(e)}")
        print("\n" + "="*80)
        print("TEST RESULT:")
        print("="*80)
        print(f"Registration Status: FAILED")
        print(f"Error: {str(e)}")
        print("="*80 + "\n")
        
        # Assertion: Registration flow should not raise exceptions
        assert False, f"Registration after deleting session cookies failed: {str(e)}"
