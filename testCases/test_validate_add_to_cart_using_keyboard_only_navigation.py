"""
Test for AddToCartFlow.validate_add_to_cart_using_keyboard_only_navigation() method.

This test validates that the entire add-to-cart workflow is fully accessible
using only keyboard interactions (TAB, ENTER) without mouse clicks.

Test Scope: UI - Accessibility Test Case
Flow Method: AddToCartFlow.validate_add_to_cart_using_keyboard_only_navigation()
"""

import pytest
from flows.addToCartFlow import AddToCartFlow
from utilities.customLogger import LoggerFactory

logger = LoggerFactory.get_logger(__name__)


@pytest.mark.ui
@pytest.mark.regression
def test_validate_add_to_cart_using_keyboard_only_navigation(driver):
    """
    Test that add-to-cart workflow is fully accessible using keyboard-only navigation.
    
    Scenario: User completes entire add-to-cart process using only keyboard (no mouse)
    Expected Behavior:
    - Search field should be accessible via keyboard
    - Search should execute with keyboard input and ENTER
    - Product selection should work via keyboard
    - Product page should load
    - Quantity field should be accessible via keyboard
    - Add to Cart button should be accessible and activatable via keyboard
    - Product should be successfully added to cart
    - Overall keyboard accessibility should be working
    
    Args:
        driver: WebDriver fixture providing browser instance
    
    Assertions:
    - Search field is accessible
    - Search executes via keyboard
    - Product selection works via keyboard
    - Quantity entry works via keyboard
    - Add to Cart button is accessible and works via keyboard
    - Product is added to cart with correct quantity
    - Keyboard accessibility is fully functional
    - Test passes
    """
    logger.info("="*80)
    logger.info("Starting test: validate_add_to_cart_using_keyboard_only_navigation")
    logger.info("="*80)
    
    # Initialize AddToCartFlow with WebDriver
    add_to_cart_flow = AddToCartFlow(driver)
    
    # Test data - product to add via keyboard navigation
    product_name = "Lenovo Thinkpad X1 Carbon"
    quantity = 1
    
    logger.info(f"Testing keyboard-only navigation: {product_name}, quantity: {quantity}")
    
    # Execute the flow method under test
    result = add_to_cart_flow.validate_add_to_cart_using_keyboard_only_navigation(product_name, quantity)
    
    logger.info(f"Flow returned result: {result}")
    
    # ===== Assertions =====
    
    print("\n" + "="*80)
    print("TEST RESULT:")
    print("="*80)
    print(f"Test Case: {result['test_case_title']}")
    print(f"Product Name: {result['product_name']}")
    print(f"Quantity Requested: {result['quantity_requested']}")
    print(f"Search Field Accessible: {result['search_field_accessible']}")
    print(f"Search Executed: {result['search_executed']}")
    print(f"Product Selection via Keyboard: {result['product_selection_via_keyboard']}")
    print(f"Product Page Accessible: {result['product_page_accessible']}")
    print(f"Quantity Field Accessible: {result['quantity_field_accessible']}")
    print(f"Quantity Entered: {result['quantity_entered']}")
    print(f"Add to Cart Button Accessible: {result['add_to_cart_button_accessible']}")
    print(f"Add to Cart via Keyboard: {result['add_to_cart_via_keyboard']}")
    print(f"Product Added to Cart: {result['product_added_to_cart']}")
    print(f"Product Quantity in Cart: {result['product_quantity_in_cart']}")
    print(f"Keyboard Accessibility Working: {result['keyboard_accessibility_working']}")
    print(f"Test Passed: {result['test_passed']}")
    print(f"Test Failure Reason: {result['test_failure_reason']}")
    print("="*80 + "\n")
    
    # Assertion 1: Search field should be accessible
    assert result['search_field_accessible'] is True, \
        f"Assertion 1: Expected search field to be accessible, but search_field_accessible={result['search_field_accessible']}"
    
    # Assertion 2: Search should execute via keyboard
    assert result['search_executed'] is True, \
        f"Assertion 2: Expected search to execute via keyboard, but search_executed={result['search_executed']}"
    
    # Assertion 3: Product selection should work via keyboard
    assert result['product_selection_via_keyboard'] is True, \
        f"Assertion 3: Expected product selection via keyboard to work, but product_selection_via_keyboard={result['product_selection_via_keyboard']}"
    
    # Assertion 4: Product page should be accessible
    assert result['product_page_accessible'] is True, \
        f"Assertion 4: Expected product page to be accessible, but product_page_accessible={result['product_page_accessible']}"
    
    # Assertion 5: Quantity field should be accessible
    assert result['quantity_field_accessible'] is True, \
        f"Assertion 5: Expected quantity field to be accessible, but quantity_field_accessible={result['quantity_field_accessible']}"
    
    # Assertion 6: Quantity should be entered via keyboard
    assert result['quantity_entered'] is True, \
        f"Assertion 6: Expected quantity to be entered via keyboard, but quantity_entered={result['quantity_entered']}"
    
    # Assertion 7: Add to Cart button should be accessible
    assert result['add_to_cart_button_accessible'] is True, \
        f"Assertion 7: Expected Add to Cart button to be accessible, but add_to_cart_button_accessible={result['add_to_cart_button_accessible']}"
    
    # Assertion 8: Add to Cart should work via keyboard
    assert result['add_to_cart_via_keyboard'] is True, \
        f"Assertion 8: Expected Add to Cart to work via keyboard, but add_to_cart_via_keyboard={result['add_to_cart_via_keyboard']}"
    
    # Assertion 9: Product should be added to cart
    assert result['product_added_to_cart'] is True, \
        f"Assertion 9: Expected product to be added to cart, but product_added_to_cart={result['product_added_to_cart']}"
    
    # Assertion 10: Product quantity should match requested quantity
    assert result['product_quantity_in_cart'] == quantity, \
        f"Assertion 10: Expected quantity {quantity}, but product_quantity_in_cart={result['product_quantity_in_cart']}"
    
    # Assertion 11: Keyboard accessibility should be working
    assert result['keyboard_accessibility_working'] is True, \
        f"Assertion 11: Expected keyboard accessibility to be working, but keyboard_accessibility_working={result['keyboard_accessibility_working']}"
    
    # Assertion 12: Overall test should pass
    assert result['test_passed'] is True, \
        f"Assertion 12: Expected test to pass, but test_passed={result['test_passed']}. Reason: {result['test_failure_reason']}"
    
    logger.info("="*80)
    logger.info("Test PASSED: validate_add_to_cart_using_keyboard_only_navigation")
    logger.info("="*80)
