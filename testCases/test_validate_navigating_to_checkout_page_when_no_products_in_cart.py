"""
Test for CheckoutFlow.validate_navigating_to_checkout_page_when_no_products_in_cart() method.

This test validates that the checkout page properly handles the scenario when a user attempts to navigate
to checkout with no products in the shopping cart, displaying an appropriate error message or warning.

Test Scope: UI - Negative Test (Empty Cart Validation)
Flow Method: CheckoutFlow.validate_navigating_to_checkout_page_when_no_products_in_cart()
"""

import pytest
from flows.checkoutFlow import CheckoutFlow
from utilities.customLogger import LoggerFactory


@pytest.mark.ui
@pytest.mark.negative
def test_validate_navigating_to_checkout_page_when_no_products_in_cart(driver):
    """
    Test checkout page behavior when cart is empty.
    
    Validates that:
    - Checkout page loads successfully
    - Error message is displayed for empty cart OR cart is identified as empty
    - Application handles empty cart appropriately
    - Test result indicates proper empty cart handling
    """
    logger = LoggerFactory.get_logger(__name__)
    
    # Initialize CheckoutFlow
    checkout_flow = CheckoutFlow(driver)
    
    # Call the Flow method - single entry point for this test
    result = checkout_flow.validate_navigating_to_checkout_page_when_no_products_in_cart()
    
    # Assertions verifying empty cart checkout behavior
    assert result is not None, "Flow method should return a result dictionary"
    
    assert result.get('test_case_title') == 'Validate navigating to checkout page when there are no products added to the Shopping Cart', \
        "Test case title should be correctly set"
    
    assert result.get('page_loaded') is True, \
        "Checkout page should load even with empty cart"
    
    assert result.get('page_title') is not None, \
        "Page title should be retrievable from checkout page"
    
    # Verify that either error is displayed OR cart is empty (proper handling)
    error_displayed = result.get('error_displayed', False)
    cart_empty = result.get('cart_empty', False)
    
    assert error_displayed or cart_empty, \
        "Either error message should be displayed or cart should be identified as empty"
    
    # If error is displayed, capture the error message
    if error_displayed:
        error_message = result.get('error_message')
        assert error_message is not None, \
            "Error message should be provided when error is displayed for empty cart"
        logger.info(f"Empty cart error message: {error_message}")
    
    # Verify test passed - empty cart handling is working
    assert result.get('test_passed') is True, \
        "Test should pass - empty cart should be properly handled"
    
    assert result.get('test_failure_reason') is None, \
        "There should be no failure reason when empty cart is properly handled"
    
    # Log test completion
    logger.info("✓ Test PASSED: Checkout page properly handles empty cart scenario")
    print("\n" + "="*80)
    print("TEST RESULT: PASSED")
    print("="*80)
    print(f"Test Case: {result.get('test_case_title')}")
    print(f"Page Title: {result.get('page_title')}")
    print(f"Page Loaded: {result.get('page_loaded')}")
    print(f"Error Displayed: {result.get('error_displayed')}")
    if result.get('error_displayed'):
        print(f"Error Message: {result.get('error_message')}")
    print(f"Cart Empty: {result.get('cart_empty')}")
    print(f"Empty Cart Handled Properly: {result.get('test_passed')}")
    print("="*80 + "\n")
