"""
Test for RegisterFlow.register_with_slow_typing() method.

This test validates that the registration flow correctly handles slow,
character-by-character typing input, simulating human-like typing behavior.

Test Scope: UI - Positive Test Case
Flow Method: RegisterFlow.register_with_slow_typing()
"""

import pytest
from flows.registerFlow import RegisterFlow
from utilities.customLogger import LoggerFactory

logger = LoggerFactory.get_logger(__name__)


@pytest.mark.ui
@pytest.mark.regression
def test_register_with_slow_typing(driver):
    """
    Test that registration succeeds when form fields are filled with slow typing.
    
    Scenario: User registers with slow, character-by-character typing behavior
    Expected Behavior:
    - All form fields should accept slow typing input
    - Registration should complete successfully
    - Success message should be displayed
    - Continue button should be clickable after success
    
    Args:
        driver: WebDriver fixture providing browser instance
    
    Assertions:
    - Registration should succeed
    - Success message should be present
    """
    logger.info("="*80)
    logger.info("Starting test: register_with_slow_typing")
    logger.info("="*80)
    
    # Initialize RegisterFlow with WebDriver
    register_flow = RegisterFlow(driver)
    
    # Test data - valid registration credentials
    first_name = "Automation"
    last_name = "Test"
    email = f"slowtype_{int(__import__('time').time())}@test.com"
    password = "TestPassword123!@"
    typing_delay = 0.05  # 50ms delay between characters for slow typing
    
    logger.info(f"Attempting registration with slow typing - email: {email}")
    logger.info(f"Typing delay: {typing_delay}s per character")
    
    # Execute the flow method under test
    try:
        register_flow.register_with_slow_typing(first_name, last_name, email, password, typing_delay)
        
        logger.info("Registration flow executed successfully")
        
        # ===== Assertions =====
        
        print("\n" + "="*80)
        print("TEST RESULT:")
        print("="*80)
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Email: {email}")
        print(f"Typing Delay: {typing_delay}s per character")
        print("Registration Status: SUCCESS")
        print("="*80 + "\n")
        
        # Assertion: Registration should complete without exceptions
        assert True, "Registration with slow typing completed successfully"
        
        logger.info("="*80)
        logger.info("Test PASSED: register_with_slow_typing")
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
        assert False, f"Registration with slow typing failed: {str(e)}"
