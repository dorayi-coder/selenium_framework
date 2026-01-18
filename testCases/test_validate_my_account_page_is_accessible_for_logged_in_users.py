"""
Test for MyAccountFlow.validate_my_account_page_is_accessible_for_logged_in_users() method.

This test validates that the My Account page is properly accessible to logged-in users and displays
all required user-specific content including customer name, welcome message, and navigation menu items.

Test Scope: UI - Access Control & User Content Test
Flow Method: MyAccountFlow.validate_my_account_page_is_accessible_for_logged_in_users()
"""

import pytest
from flows.myAccountFlow import MyAccountFlow
from utilities.customLogger import LoggerFactory


@pytest.mark.ui
@pytest.mark.regression
def test_validate_my_account_page_is_accessible_for_logged_in_users(driver):
    """
    Test My Account page accessibility for logged-in users.
    
    Validates that:
    - My Account page loads successfully
    - Page title is retrievable
    - Customer name is displayed (indicating logged-in status)
    - Welcome message is shown
    - User is verified as logged in
    - Account menu items are available
    - Menu items count is greater than zero
    - Page displays proper user-specific content
    """
    logger = LoggerFactory.get_logger(__name__)
    
    # Initialize MyAccountFlow
    account_flow = MyAccountFlow(driver)
    
    # Call the Flow method - single entry point for this test
    result = account_flow.validate_my_account_page_is_accessible_for_logged_in_users()
    
    # Assertions verifying My Account page accessibility for logged-in users
    assert result is not None, "Flow method should return a result dictionary"
    
    assert result.get('test_case_title') == 'Verify my account page is accessible for logged in users', \
        "Test case title should be correctly set"
    
    assert result.get('page_loaded') is True, \
        "My Account page should load successfully for logged-in user"
    
    assert result.get('page_title') is not None, \
        "Page title should be retrievable on My Account page"
    
    assert result.get('customer_name') is not None, \
        "Customer name should be displayed (indicates logged-in user)"
    
    customer_name = result.get('customer_name', '')
    assert len(customer_name) > 0, \
        "Customer name should not be empty for logged-in user"
    
    assert result.get('welcome_message') is not None, \
        "Welcome message should be displayed for logged-in user"
    
    assert result.get('user_logged_in') is True, \
        "User should be identified as logged in"
    
    assert result.get('menu_items_available') is True, \
        "Account menu items should be available for logged-in user"
    
    assert result.get('menu_items_count') > 0, \
        "Menu items count should be greater than zero"
    
    assert result.get('test_passed') is True, \
        "Test should pass - My Account page should be accessible for logged-in users"
    
    assert result.get('test_failure_reason') is None, \
        "There should be no failure reason when page is properly accessible"
    
    # Log test completion with accessibility details
    menu_count = result.get('menu_items_count', 0)
    logger.info(f"✓ Test PASSED: My Account page accessible for logged-in user {customer_name} with {menu_count} menu items")
    print("\n" + "="*80)
    print("TEST RESULT: PASSED")
    print("="*80)
    print(f"Test Case: {result.get('test_case_title')}")
    print(f"Page Loaded: {result.get('page_loaded')}")
    print(f"Page Title: {result.get('page_title')}")
    print(f"Customer Name: {result.get('customer_name')}")
    print(f"Welcome Message: {result.get('welcome_message')}")
    print(f"User Logged In: {result.get('user_logged_in')}")
    print(f"Menu Items Available: {result.get('menu_items_available')}")
    print(f"Menu Items Count: {result.get('menu_items_count')}")
    print(f"Page Accessible for Logged-In User: {result.get('test_passed')}")
    print("User Context: Authenticated and authorized for account access")
    print("="*80 + "\n")
