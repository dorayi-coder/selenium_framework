"""
Test for MyAccountFlow.verify_my_account_page_loads_correct_user_information() method.

This test validates that the My Account page correctly loads and displays the user's profile information
including customer name and welcome message, ensuring proper personalization of the account experience.

Test Scope: UI - User Information Display Test
Flow Method: MyAccountFlow.verify_my_account_page_loads_correct_user_information()
"""

import pytest
from flows.myAccountFlow import MyAccountFlow
from utilities.customLogger import LoggerFactory


@pytest.mark.ui
@pytest.mark.regression
def test_verify_my_account_page_loads_correct_user_information(driver):
    """
    Test that My Account page loads correct user information.
    
    Validates that:
    - My Account page loads successfully
    - Customer name is displayed
    - Customer name is not empty
    - Welcome message is shown
    - Welcome message is not empty
    - Both required user information elements are present
    - Test passes indicating proper user data display
    """
    logger = LoggerFactory.get_logger(__name__)
    
    # Initialize MyAccountFlow
    account_flow = MyAccountFlow(driver)
    
    # Call the Flow method - single entry point for this test
    result = account_flow.verify_my_account_page_loads_correct_user_information()
    
    # Assertions verifying user information display on My Account page
    assert result is not None, "Flow method should return a result dictionary"
    
    assert result.get('test_case_title') == "Verify 'My Account Page' loads correct user information", \
        "Test case title should be correctly set"
    
    assert result.get('customer_name') is not None, \
        "Customer name should be retrieved and displayed"
    
    customer_name = result.get('customer_name', '')
    assert len(customer_name) > 0, \
        "Customer name should not be empty"
    
    assert result.get('welcome_message') is not None, \
        "Welcome message should be retrieved and displayed"
    
    welcome_message = result.get('welcome_message', '')
    assert len(welcome_message) > 0, \
        "Welcome message should not be empty"
    
    assert result.get('name_present') is True, \
        "Name presence flag should indicate customer name is present"
    
    assert result.get('welcome_present') is True, \
        "Welcome message presence flag should indicate welcome message is present"
    
    assert result.get('test_passed') is True, \
        "Test should pass - user information should be correctly loaded and displayed"
    
    assert result.get('test_failure_reason') is None, \
        "There should be no failure reason when user information is properly displayed"
    
    # Log test completion with user information details
    logger.info(f"✓ Test PASSED: My Account page correctly displays user information for {customer_name}")
    print("\n" + "="*80)
    print("TEST RESULT: PASSED")
    print("="*80)
    print(f"Test Case: {result.get('test_case_title')}")
    print(f"Customer Name: {result.get('customer_name')}")
    print(f"Name Present: {result.get('name_present')}")
    print(f"Welcome Message: {result.get('welcome_message')}")
    print(f"Welcome Present: {result.get('welcome_present')}")
    print(f"User Information Loaded: {result.get('test_passed')}")
    print("Account Personalization: User data correctly displayed")
    print("="*80 + "\n")
