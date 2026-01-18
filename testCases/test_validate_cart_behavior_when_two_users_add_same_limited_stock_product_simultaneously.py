"""
Test for AddToCartFlow.validate_cart_behavior_when_two_users_add_same_limited_stock_product_simultaneously() method.

This test validates that the cart system properly handles inventory constraints when multiple users
attempt to add the same limited-stock product simultaneously.

Test Scope: UI - Inventory Management Test Case
Flow Method: AddToCartFlow.validate_cart_behavior_when_two_users_add_same_limited_stock_product_simultaneously()
"""

import pytest
from flows.addToCartFlow import AddToCartFlow
from utilities.customLogger import LoggerFactory

logger = LoggerFactory.get_logger(__name__)


@pytest.mark.ui
@pytest.mark.regression
def test_validate_cart_behavior_when_two_users_add_same_limited_stock_product_simultaneously(driver):
    """
    Test that cart system correctly handles inventory when two users add same limited-stock product simultaneously.
    
    Scenario: Two users attempt to add the same product with limited stock within the same session
    Expected Behavior:
    - Both users can add product to their respective carts
    - Stock limit should be respected
    - Inventory conflict should not occur (total quantity should not exceed available stock)
    - System should properly track individual user quantities
    - Test should validate inventory management constraints
    
    Args:
        driver: WebDriver fixture providing browser instance
    
    Assertions:
    - Both users should successfully add product to cart
    - Stock limit should be respected
    - Total quantity should not exceed available stock
    - No inventory conflict should be detected
    - Test should pass inventory validation
    """
    logger.info("="*80)
    logger.info("Starting test: validate_cart_behavior_when_two_users_add_same_limited_stock_product_simultaneously")
    logger.info("="*80)
    
    # Initialize AddToCartFlow with WebDriver
    add_to_cart_flow = AddToCartFlow(driver)
    
    # Test data - limited stock product scenario
    product_name = "Lenovo Thinkpad X1 Carbon"
    user1_quantity = 1
    user2_quantity = 1
    total_available_stock = 2
    
    logger.info(f"Testing inventory management for limited-stock product: {product_name}")
    logger.info(f"User 1 quantity: {user1_quantity}, User 2 quantity: {user2_quantity}, Total stock: {total_available_stock}")
    
    # Execute the flow method under test
    result = add_to_cart_flow.validate_cart_behavior_when_two_users_add_same_limited_stock_product_simultaneously(
        product_name,
        user1_quantity=user1_quantity,
        user2_quantity=user2_quantity,
        total_available_stock=total_available_stock
    )
    
    logger.info(f"Flow returned result: {result}")
    
    # ===== Assertions =====
    
    print("\n" + "="*80)
    print("TEST RESULT:")
    print("="*80)
    print(f"Test Case: {result['test_case_title']}")
    print(f"Product Name: {result['product_name']}")
    print(f"Total Available Stock: {result['total_available_stock']}")
    print(f"User 1 Quantity Requested: {result['user1_quantity_requested']}")
    print(f"User 2 Quantity Requested: {result['user2_quantity_requested']}")
    print(f"User 1 Success: {result['user1_success']}")
    print(f"User 1 in Cart: {result['user1_in_cart']}")
    print(f"User 1 Quantity in Cart: {result['user1_quantity_in_cart']}")
    print(f"User 2 Success: {result['user2_success']}")
    print(f"User 2 in Cart: {result['user2_in_cart']}")
    print(f"User 2 Quantity in Cart: {result['user2_quantity_in_cart']}")
    print(f"Total Quantity in Both Carts: {result['total_quantity_in_both_carts']}")
    print(f"Inventory Conflict Detected: {result['inventory_conflict_detected']}")
    print(f"Stock Limit Respected: {result['stock_limit_respected']}")
    print(f"Test Passed: {result['test_passed']}")
    print(f"Test Failure Reason: {result['test_failure_reason']}")
    print("="*80 + "\n")
    
    # Assertion 1: User 1 should successfully add product to cart
    assert result['user1_success'] is True, \
        f"Assertion 1: Expected User 1 to successfully add product, but user1_success={result['user1_success']}"
    
    # Assertion 2: User 1 product should be in cart
    assert result['user1_in_cart'] is True, \
        f"Assertion 2: Expected User 1 product to be in cart, but user1_in_cart={result['user1_in_cart']}"
    
    # Assertion 3: User 1 quantity should match requested
    assert result['user1_quantity_in_cart'] == user1_quantity, \
        f"Assertion 3: Expected User 1 quantity {user1_quantity}, but got {result['user1_quantity_in_cart']}"
    
    # Assertion 4: User 2 should successfully add product to cart
    assert result['user2_success'] is True, \
        f"Assertion 4: Expected User 2 to successfully add product, but user2_success={result['user2_success']}"
    
    # Assertion 5: User 2 product should be in cart
    assert result['user2_in_cart'] is True, \
        f"Assertion 5: Expected User 2 product to be in cart, but user2_in_cart={result['user2_in_cart']}"
    
    # Assertion 6: User 2 quantity should match requested
    assert result['user2_quantity_in_cart'] == user2_quantity, \
        f"Assertion 6: Expected User 2 quantity {user2_quantity}, but got {result['user2_quantity_in_cart']}"
    
    # Assertion 7: Stock limit should be respected
    assert result['stock_limit_respected'] is True, \
        f"Assertion 7: Expected stock limit to be respected, but stock_limit_respected={result['stock_limit_respected']}"
    
    # Assertion 8: No inventory conflict should be detected
    assert result['inventory_conflict_detected'] is False, \
        f"Assertion 8: Expected no inventory conflict, but inventory_conflict_detected={result['inventory_conflict_detected']}"
    
    # Assertion 9: Total quantity should not exceed available stock
    assert result['total_quantity_in_both_carts'] <= total_available_stock, \
        f"Assertion 9: Expected total quantity ({result['total_quantity_in_both_carts']}) to not exceed stock ({total_available_stock})"
    
    # Assertion 10: Overall test should pass
    assert result['test_passed'] is True, \
        f"Assertion 10: Expected test to pass, but test_passed={result['test_passed']}. Reason: {result['test_failure_reason']}"
    
    logger.info("="*80)
    logger.info("Test PASSED: validate_cart_behavior_when_two_users_add_same_limited_stock_product_simultaneously")
    logger.info("="*80)
