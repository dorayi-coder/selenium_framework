"""
Test for OrderConfirmationFlow.verify_order_confirmation_page_is_displayed_after_successful_order_placement() method.

This test validates that the Order Confirmation page is properly displayed to users after they complete
a successful order placement, with all required confirmation details visible and accessible.

Test Scope: UI - Order Confirmation Page Display Test
Flow Method: OrderConfirmationFlow.verify_order_confirmation_page_is_displayed_after_successful_order_placement()
"""

import pytest
from flows.orderConfirmationFlow import OrderConfirmationFlow
from utilities.customLogger import LoggerFactory


@pytest.mark.ui
@pytest.mark.regression
def test_verify_order_confirmation_page_is_displayed_after_successful_order_placement(driver):
    """
    Test that Order Confirmation page is displayed after successful order placement.
    
    Validates that:
    - Order Confirmation page loads successfully
    - Page title is captured and accessible
    - Success message is displayed to user
    - Order number is present and not empty
    - Confirmation details are populated
    - All essential confirmation elements are present
    - User receives clear order confirmation
    - Test passes indicating proper confirmation page display
    - No failure reason when all elements present
    """
    logger = LoggerFactory.get_logger(__name__)
    
    # Initialize OrderConfirmationFlow
    confirmation_flow = OrderConfirmationFlow(driver)
    
    # Call the Flow method - single entry point for this test
    result = confirmation_flow.verify_order_confirmation_page_is_displayed_after_successful_order_placement()
    
    # Assertions verifying order confirmation page display
    assert result is not None, "Flow method should return a result dictionary"
    
    assert result.get('test_case_title') == "Verify Order Confirmation page is displayed after successful order placement", \
        "Test case title should be correctly set"
    
    assert result.get('page_title') is not None, \
        "Page title should be captured"
    
    page_title = result.get('page_title', '')
    assert len(page_title) > 0, \
        "Page title should not be empty"
    
    assert result.get('page_loaded') is True, \
        "Confirmation page should be loaded successfully"
    
    assert result.get('success_message_displayed') is not None, \
        "Success message display flag should be set"
    
    assert result.get('success_message_displayed') is True, \
        "Success message should be displayed on confirmation page"
    
    assert result.get('order_number') is not None, \
        "Order number should be captured from confirmation page"
    
    order_number = result.get('order_number', '')
    assert len(str(order_number)) > 0, \
        "Order number should not be empty"
    
    assert result.get('confirmation_details_present') is not None, \
        "Confirmation details presence flag should be set"
    
    assert result.get('confirmation_details_present') is True, \
        "Confirmation details should be present on the page"
    
    assert result.get('test_passed') is True, \
        "Test should pass - confirmation page should be properly displayed"
    
    assert result.get('test_failure_reason') is None, \
        "There should be no failure reason when confirmation page is properly displayed"
    
    # Verify consistency of confirmation page elements
    all_elements_present = (
        result.get('success_message_displayed') and 
        result.get('confirmation_details_present')
    )
    assert all_elements_present, \
        "All confirmation page elements should be present and visible"
    
    # Log test completion with order confirmation details
    logger.info(f"✓ Test PASSED: Order Confirmation page displayed successfully for order {order_number}")
    print("\n" + "="*80)
    print("TEST RESULT: PASSED")
    print("="*80)
    print(f"Test Case: {result.get('test_case_title')}")
    print(f"Page Title: {result.get('page_title')}")
    print(f"Page Loaded: {result.get('page_loaded')}")
    print(f"Success Message: {result.get('success_message_displayed')}")
    print(f"Order Number: {result.get('order_number')}")
    print(f"Confirmation Details: {result.get('confirmation_details_present')}")
    print(f"Order Status: Successfully placed with confirmation displayed")
    print(f"User Experience: Complete order confirmation received")
    print("="*80 + "\n")
