"""
Test for CheckoutFlow.verify_checkout_page_opens_with_items_present_in_shopping_cart() method.

This test validates that the checkout page opens successfully when there are items present in the shopping cart,
and that the cart contents are properly displayed with no error messages.

Test Scope: UI - Positive Test (Items Present Validation)
Flow Method: CheckoutFlow.verify_checkout_page_opens_with_items_present_in_shopping_cart()
"""

import pytest
from flows.checkoutFlow import CheckoutFlow
from utilities.customLogger import LoggerFactory


@pytest.mark.ui
@pytest.mark.regression
def test_verify_checkout_page_opens_with_items_present_in_shopping_cart(driver):
    """
    Test checkout page opens successfully with items in cart.
    
    Validates that:
    - Checkout page loads successfully
    - Cart has items present
    - No error messages are displayed
    - Cart items count is greater than zero
    - Page title is retrievable
    - Overall test passes with items properly displayed
    """
    logger = LoggerFactory.get_logger(__name__)
    
    # Initialize CheckoutFlow
    checkout_flow = CheckoutFlow(driver)
    
    # Call the Flow method - single entry point for this test
    result = checkout_flow.verify_checkout_page_opens_with_items_present_in_shopping_cart()
    
    # Assertions verifying checkout page opens with items in cart
    assert result is not None, "Flow method should return a result dictionary"
    
    assert result.get('test_case_title') == 'Verify Checkout page opens with items present in Shopping Cart', \
        "Test case title should be correctly set"
    
    assert result.get('page_loaded') is True, \
        "Checkout page should load successfully when items are in cart"
    
    assert result.get('page_title') is not None, \
        "Page title should be retrievable from checkout page"
    
    assert result.get('cart_has_items') is True, \
        "Cart should have items present"
    
    assert result.get('cart_items_count') > 0, \
        "Cart items count should be greater than zero"
    
    assert result.get('error_displayed') is False, \
        "No error message should be displayed when items are in cart"
    
    assert result.get('test_passed') is True, \
        "Test should pass - checkout page should open successfully with items in cart"
    
    assert result.get('test_failure_reason') is None, \
        "There should be no failure reason when checkout page opens with items"
    
    # Log test completion with cart details
    cart_count = result.get('cart_items_count', 0)
    logger.info(f"✓ Test PASSED: Checkout page opened successfully with {cart_count} item(s) in cart")
    print("\n" + "="*80)
    print("TEST RESULT: PASSED")
    print("="*80)
    print(f"Test Case: {result.get('test_case_title')}")
    print(f"Page Title: {result.get('page_title')}")
    print(f"Page Loaded: {result.get('page_loaded')}")
    print(f"Cart Has Items: {result.get('cart_has_items')}")
    print(f"Cart Items Count: {result.get('cart_items_count')}")
    print(f"Error Displayed: {result.get('error_displayed')}")
    print(f"Checkout Page Opened Successfully: {result.get('test_passed')}")
    print("="*80 + "\n")
