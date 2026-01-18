"""
Test for AddToCartFlow.verify_product_in_cart() method.

This test validates that products can be verified as present in the shopping cart
with correct product information and quantity.

Test Scope: UI - Cart Verification Test Case
Flow Method: AddToCartFlow.verify_product_in_cart()
"""

import pytest
from flows.addToCartFlow import AddToCartFlow
from utilities.customLogger import LoggerFactory

logger = LoggerFactory.get_logger(__name__)


@pytest.mark.ui
@pytest.mark.regression
def test_verify_product_in_cart(driver):
    """
    Test that a product can be verified as present in the shopping cart.
    
    Scenario: Verify that a product added to cart can be found and verified
    Expected Behavior:
    - Cart page should be loaded and accessible
    - Product should be found in cart
    - Product quantity should be retrievable
    - All products in cart should be listed
    - Verification should pass
    
    Args:
        driver: WebDriver fixture providing browser instance
    
    Assertions:
    - Product should be found in cart
    - Verification should pass
    - Cart should contain at least one item
    - Product quantity should be greater than zero
    """
    logger.info("="*80)
    logger.info("Starting test: verify_product_in_cart")
    logger.info("="*80)
    
    # Initialize AddToCartFlow with WebDriver
    add_to_cart_flow = AddToCartFlow(driver)
    
    # Test data - product name to verify in cart
    # Note: In a real scenario, a product would be added first, then verified
    # This test assumes a product is already in the cart from setup or previous steps
    product_name = "Lenovo Thinkpad X1 Carbon"  # Common product in nopCommerce demo
    
    logger.info(f"Verifying product in cart: {product_name}")
    
    # Execute the flow method under test
    result = add_to_cart_flow.verify_product_in_cart(product_name)
    
    logger.info(f"Flow returned result: {result}")
    
    # ===== Assertions =====
    
    print("\n" + "="*80)
    print("TEST RESULT:")
    print("="*80)
    print(f"Product Found in Cart: {result['product_found_in_cart']}")
    print(f"Cart Item Count: {result['cart_item_count']}")
    print(f"Product Quantity: {result['product_quantity']}")
    print(f"All Products in Cart: {result['all_products_in_cart']}")
    print(f"Verification Passed: {result['verification_passed']}")
    print("="*80 + "\n")
    
    # Assertion 1: Verification should pass
    assert result['verification_passed'] is True, \
        f"Assertion 1: Expected verification to pass, but verification_passed={result['verification_passed']}"
    
    # Assertion 2: Product should be found in cart
    assert result['product_found_in_cart'] is True, \
        f"Assertion 2: Expected product '{product_name}' to be found in cart, but product_found_in_cart={result['product_found_in_cart']}"
    
    # Assertion 3: Cart should have at least one item
    assert result['cart_item_count'] > 0, \
        f"Assertion 3: Expected cart to contain items, but cart_item_count={result['cart_item_count']}"
    
    # Assertion 4: Product quantity should be greater than zero
    assert result['product_quantity'] > 0, \
        f"Assertion 4: Expected product quantity to be greater than 0, but product_quantity={result['product_quantity']}"
    
    # Assertion 5: All products list should not be empty
    assert len(result['all_products_in_cart']) > 0, \
        f"Assertion 5: Expected products list to be populated, but got {len(result['all_products_in_cart'])} products"
    
    logger.info("="*80)
    logger.info("Test PASSED: verify_product_in_cart")
    logger.info("="*80)
