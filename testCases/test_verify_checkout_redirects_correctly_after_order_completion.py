"""
Test for CheckoutFlow.verify_checkout_redirects_correctly_after_order_completion() method.

This test validates that after successfully placing an order during checkout, the application redirects
the user to the appropriate confirmation or success page, completing the e-commerce transaction journey.

Test Scope: UI - Positive Test (Post-Order Redirect Validation)
Flow Method: CheckoutFlow.verify_checkout_redirects_correctly_after_order_completion()
"""

import pytest
from flows.checkoutFlow import CheckoutFlow
from utilities.customLogger import LoggerFactory


@pytest.mark.ui
@pytest.mark.regression
def test_verify_checkout_redirects_correctly_after_order_completion(driver):
    """
    Test checkout redirects successfully after order is placed.
    
    Validates that:
    - Checkout page loads successfully
    - Order placement is executed
    - Page redirects after order completion
    - URL changes to confirmation/success page OR confirmation page becomes visible
    - Application properly completes the transaction workflow
    - Test confirms redirect behavior is working
    """
    logger = LoggerFactory.get_logger(__name__)
    
    # Initialize CheckoutFlow
    checkout_flow = CheckoutFlow(driver)
    
    # Call the Flow method - single entry point for this test
    result = checkout_flow.verify_checkout_redirects_correctly_after_order_completion()
    
    # Assertions verifying checkout redirect after order completion
    assert result is not None, "Flow method should return a result dictionary"
    
    assert result.get('test_case_title') == 'Verify Checkout redirects correctly after order completion', \
        "Test case title should be correctly set"
    
    assert result.get('page_loaded') is True, \
        "Checkout page should load successfully before order placement"
    
    assert result.get('initial_url') is not None, \
        "Initial checkout URL should be captured before order placement"
    
    assert result.get('final_url') is not None, \
        "Final URL should be captured after order placement"
    
    # Verify either URL changed OR confirmation page is visible (one or both redirect indicators)
    url_changed = result.get('url_changed', False)
    confirmation_visible = result.get('confirmation_visible', False)
    
    assert url_changed or confirmation_visible, \
        "Either URL should change to confirmation page OR confirmation page should become visible after order completion"
    
    # Log redirect details
    if url_changed:
        initial_url = result.get('initial_url', 'N/A')
        final_url = result.get('final_url', 'N/A')
        logger.info(f"URL redirect detected: {initial_url} → {final_url}")
    
    if confirmation_visible:
        logger.info("Confirmation page visibility detected")
    
    assert result.get('test_passed') is True, \
        "Test should pass - checkout should redirect correctly after order completion"
    
    assert result.get('test_failure_reason') is None, \
        "There should be no failure reason when redirect works correctly"
    
    # Log test completion with redirect confirmation
    logger.info("✓ Test PASSED: Checkout successfully redirected after order placement")
    print("\n" + "="*80)
    print("TEST RESULT: PASSED")
    print("="*80)
    print(f"Test Case: {result.get('test_case_title')}")
    print(f"Page Loaded: {result.get('page_loaded')}")
    print(f"Initial URL: {result.get('initial_url')}")
    print(f"Final URL: {result.get('final_url')}")
    print(f"URL Changed: {result.get('url_changed')}")
    print(f"Confirmation Page Visible: {result.get('confirmation_visible')}")
    print(f"Redirect Successful: {result.get('test_passed')}")
    print("Transaction Workflow Completed: Order placed and user redirected")
    print("="*80 + "\n")
