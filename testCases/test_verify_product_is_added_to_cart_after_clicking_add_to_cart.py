"""
Test for AddToCartFlow.verify_product_is_added_to_cart_after_clicking_add_to_cart() method.

This test validates that a product is successfully added to the cart with the correct
quantity after clicking the "Add to Cart" button.

Test Scope: UI - Cart Addition Verification Test Case
Flow Method: AddToCartFlow.verify_product_is_added_to_cart_after_clicking_add_to_cart()
"""

import pytest
from flows.addToCartFlow import AddToCartFlow
from utilities.customLogger import LoggerFactory

logger = LoggerFactory.get_logger(__name__)


@pytest.mark.ui
@pytest.mark.regression
def test_verify_product_is_added_to_cart_after_clicking_add_to_cart(driver):
    """
    Test that a product is successfully added to cart with correct quantity after clicking 'Add to Cart'.
    
    Scenario: User searches for a product, enters quantity, clicks Add to Cart, and verifies it appears in cart
    Expected Behavior:
    - Add-to-cart workflow should succeed
    - Product should be found in cart
    - Product quantity in cart should match the quantity requested
    - Confirmation message should be displayed
    - Cart item count should be updated
    
    Args:
        driver: WebDriver fixture providing browser instance
    
    Assertions:
    - Add-to-cart workflow should succeed
    - Product should be found in cart after add-to-cart action
    - Quantity in cart should match requested quantity
    - Test result should indicate success
    """
    logger.info("="*80)
    logger.info("Starting test: verify_product_is_added_to_cart_after_clicking_add_to_cart")
    logger.info("="*80)
    
    # Initialize AddToCartFlow with WebDriver
    add_to_cart_flow = AddToCartFlow(driver)
    
    # Test data - product to add and quantity
    product_name = "Lenovo Thinkpad X1 Carbon"
    quantity = 1
    
    logger.info(f"Attempting to add product to cart: {product_name}, quantity: {quantity}")
    
    # Execute the flow method under test
    result = add_to_cart_flow.verify_product_is_added_to_cart_after_clicking_add_to_cart(product_name, quantity)
    
    logger.info(f"Flow returned result: {result}")
    
    # ===== Assertions =====
    
    print("\n" + "="*80)
    print("TEST RESULT:")
    print("="*80)
    print(f"Test Case: {result['test_case_title']}")
    print(f"Product Name: {result['product_name']}")
    print(f"Quantity Added: {result['quantity_added']}")
    print(f"Add-to-Cart Workflow Success: {result['add_to_cart_workflow_success']}")
    print(f"Confirmation Message: {result['confirmation_message']}")
    print(f"Product Found in Cart: {result['product_found_in_cart']}")
    print(f"Product Quantity in Cart: {result['product_quantity_in_cart']}")
    print(f"Quantity Matches: {result['quantity_matches']}")
    print(f"Cart Item Count: {result['cart_item_count']}")
    print(f"Test Passed: {result['test_passed']}")
    print(f"Test Failure Reason: {result['test_failure_reason']}")
    print("="*80 + "\n")
    
    # Assertion 1: Add-to-cart workflow should succeed
    assert result['add_to_cart_workflow_success'] is True, \
        f"Assertion 1: Expected add-to-cart workflow to succeed, but add_to_cart_workflow_success={result['add_to_cart_workflow_success']}"
    
    # Assertion 2: Product should be found in cart
    assert result['product_found_in_cart'] is True, \
        f"Assertion 2: Expected product '{product_name}' to be found in cart, but product_found_in_cart={result['product_found_in_cart']}"
    
    # Assertion 3: Quantity should match
    assert result['quantity_matches'] is True, \
        f"Assertion 3: Expected quantity to match (requested: {quantity}, in cart: {result['product_quantity_in_cart']}), but quantity_matches={result['quantity_matches']}"
    
    # Assertion 4: Overall test should pass
    assert result['test_passed'] is True, \
        f"Assertion 4: Expected test to pass, but test_passed={result['test_passed']}. Reason: {result['test_failure_reason']}"
    
    # Assertion 5: Confirmation message should be present
    assert result['confirmation_message'] is not None, \
        f"Assertion 5: Expected confirmation message to be present, but got None"
    
    # Assertion 6: Cart item count should be greater than zero
    assert result['cart_item_count'] > 0, \
        f"Assertion 6: Expected cart item count to be greater than 0, but cart_item_count={result['cart_item_count']}"
    
    logger.info("="*80)
    logger.info("Test PASSED: verify_product_is_added_to_cart_after_clicking_add_to_cart")
    logger.info("="*80)
