"""
Test for AddToCartFlow.verify_cart_rejects_zero_quantity_input() method.

This test validates that the cart system properly rejects zero quantity input
and prevents products from being added with invalid quantities.

Test Scope: UI - Input Validation Test Case
Flow Method: AddToCartFlow.verify_cart_rejects_zero_quantity_input()
"""

import pytest
from flows.addToCartFlow import AddToCartFlow
from utilities.customLogger import LoggerFactory

logger = LoggerFactory.get_logger(__name__)


@pytest.mark.ui
@pytest.mark.negative
@pytest.mark.regression
def test_verify_cart_rejects_zero_quantity_input(driver):
    """
    Test that cart system rejects zero quantity input and prevents invalid additions.
    
    Scenario: User attempts to add a product with zero quantity to cart
    Expected Behavior:
    - Zero quantity should be rejected by the system
    - Add to Cart button should be disabled or non-functional
    - Product should NOT be added to cart with zero quantity
    - Input validation should prevent invalid submission
    - System should maintain data integrity
    
    Args:
        driver: WebDriver fixture providing browser instance
    
    Assertions:
    - Zero quantity input should be rejected
    - Add to Cart button should be disabled
    - Product should not be added to cart
    - Input validation should be working
    - Test should pass zero quantity validation
    """
    logger.info("="*80)
    logger.info("Starting test: verify_cart_rejects_zero_quantity_input")
    logger.info("="*80)
    
    # Initialize AddToCartFlow with WebDriver
    add_to_cart_flow = AddToCartFlow(driver)
    
    # Test data - product to attempt adding with zero quantity
    product_name = "Lenovo Thinkpad X1 Carbon"
    
    logger.info(f"Attempting to add product with zero quantity: {product_name}")
    
    # Execute the flow method under test
    result = add_to_cart_flow.verify_cart_rejects_zero_quantity_input(product_name)
    
    logger.info(f"Flow returned result: {result}")
    
    # ===== Assertions =====
    
    print("\n" + "="*80)
    print("TEST RESULT:")
    print("="*80)
    print(f"Test Case: {result['test_case_title']}")
    print(f"Product Name: {result['product_name']}")
    print(f"Zero Quantity Attempted: {result['zero_quantity_attempted']}")
    print(f"Search Executed: {result['search_executed']}")
    print(f"Product Selected: {result['product_selected']}")
    print(f"Zero Quantity Input Accepted: {result['zero_quantity_input_accepted']}")
    print(f"Add to Cart Button Disabled: {result['add_to_cart_button_disabled']}")
    print(f"Add to Cart Executed: {result['add_to_cart_executed']}")
    print(f"Product Added to Cart: {result['product_added_to_cart']}")
    print(f"Zero Quantity Rejected: {result['zero_quantity_rejected']}")
    print(f"Input Validation Working: {result['input_validation_working']}")
    print(f"Test Passed: {result['test_passed']}")
    print(f"Test Failure Reason: {result['test_failure_reason']}")
    print("="*80 + "\n")
    
    # Assertion 1: Search should be executed
    assert result['search_executed'] is True, \
        f"Assertion 1: Expected search to be executed, but search_executed={result['search_executed']}"
    
    # Assertion 2: Product should be selected
    assert result['product_selected'] is True, \
        f"Assertion 2: Expected product to be selected, but product_selected={result['product_selected']}"
    
    # Assertion 3: Zero quantity input should be rejected
    assert result['zero_quantity_rejected'] is True, \
        f"Assertion 3: Expected zero quantity to be rejected, but zero_quantity_rejected={result['zero_quantity_rejected']}"
    
    # Assertion 4: Add to Cart button should be disabled OR add execution should not occur
    assert result['add_to_cart_button_disabled'] is True or result['add_to_cart_executed'] is False, \
        f"Assertion 4: Expected button to be disabled or add to cart to not execute, but button_disabled={result['add_to_cart_button_disabled']}, add_executed={result['add_to_cart_executed']}"
    
    # Assertion 5: Product should NOT be added to cart
    assert result['product_added_to_cart'] is False, \
        f"Assertion 5: Expected product to NOT be added with zero quantity, but product_added_to_cart={result['product_added_to_cart']}"
    
    # Assertion 6: Input validation should be working
    assert result['input_validation_working'] is True, \
        f"Assertion 6: Expected input validation to be working, but input_validation_working={result['input_validation_working']}"
    
    # Assertion 7: Overall test should pass
    assert result['test_passed'] is True, \
        f"Assertion 7: Expected test to pass, but test_passed={result['test_passed']}. Reason: {result['test_failure_reason']}"
    
    logger.info("="*80)
    logger.info("Test PASSED: verify_cart_rejects_zero_quantity_input")
    logger.info("="*80)
