"""
Test for MyAccountFlow.validate_navigating_to_my_account_page_from_order_success_page() method.

This test validates that users can successfully navigate to the My Account page from the Order Success page
and that their account information is properly displayed with all relevant menu options available.

Test Scope: UI - Navigation & Account Display Test
Flow Method: MyAccountFlow.validate_navigating_to_my_account_page_from_order_success_page()
"""

import pytest
from flows.myAccountFlow import MyAccountFlow
from utilities.customLogger import LoggerFactory


@pytest.mark.ui
@pytest.mark.regression
def test_validate_navigating_to_my_account_page_from_order_success_page(driver):
    """
    Test navigation to My Account page from Order Success page.
    
    Validates that:
    - My Account page loads successfully after order completion
    - Page title is available
    - Customer name is displayed
    - Welcome message is shown
    - Account menu items are populated
    - Customer information is present
    - Navigation from order success to account page works
    """
    logger = LoggerFactory.get_logger(__name__)
    
    # Initialize MyAccountFlow
    account_flow = MyAccountFlow(driver)
    
    # Call the Flow method - single entry point for this test
    result = account_flow.validate_navigating_to_my_account_page_from_order_success_page()
    
    # Assertions verifying navigation to My Account page after order completion
    assert result is not None, "Flow method should return a result dictionary"
    
    assert result.get('test_case_title') == "Validate navigating to 'My Account' page from the 'Order Success' page", \
        "Test case title should be correctly set"
    
    assert result.get('page_loaded') is True, \
        "My Account page should load successfully after order completion"
    
    assert result.get('page_title') is not None, \
        "Page title should be retrievable on My Account page"
    
    assert result.get('customer_name') is not None, \
        "Customer name should be displayed on My Account page"
    
    customer_name = result.get('customer_name', '')
    assert len(customer_name) > 0, \
        "Customer name should not be empty"
    
    assert result.get('welcome_message') is not None, \
        "Welcome message should be displayed for the customer"
    
    assert result.get('customer_info_present') is True, \
        "Customer information should be present on the page"
    
    assert result.get('menu_items_count') > 0, \
        "Account menu items should be available and populated"
    
    assert result.get('test_passed') is True, \
        "Test should pass - navigation from order success to account should work"
    
    assert result.get('test_failure_reason') is None, \
        "There should be no failure reason when navigation works correctly"
    
    # Log test completion with navigation details
    menu_count = result.get('menu_items_count', 0)
    logger.info(f"✓ Test PASSED: Successfully navigated to My Account page for {customer_name} with {menu_count} menu items")
    print("\n" + "="*80)
    print("TEST RESULT: PASSED")
    print("="*80)
    print(f"Test Case: {result.get('test_case_title')}")
    print(f"Page Loaded: {result.get('page_loaded')}")
    print(f"Page Title: {result.get('page_title')}")
    print(f"Customer Name: {result.get('customer_name')}")
    print(f"Welcome Message: {result.get('welcome_message')}")
    print(f"Menu Items Available: {result.get('menu_items_count')}")
    print(f"Customer Info Present: {result.get('customer_info_present')}")
    print(f"Navigation Successful: {result.get('test_passed')}")
    print("Navigation Journey: Order Success → My Account Page")
    print("="*80 + "\n")
