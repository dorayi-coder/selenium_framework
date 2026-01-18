"""
Test for CheckoutFlow.verify_checkout_rejects_missing_mandatory_billing_fields() method.

This test validates that the checkout process properly rejects form submission when mandatory billing fields
are missing, displaying an appropriate error message to guide the user to fill required information.

Test Scope: UI - Negative Test (Mandatory Field Validation)
Flow Method: CheckoutFlow.verify_checkout_rejects_missing_mandatory_billing_fields()
"""

import pytest
from flows.checkoutFlow import CheckoutFlow
from utilities.customLogger import LoggerFactory


@pytest.mark.ui
@pytest.mark.negative
def test_verify_checkout_rejects_missing_mandatory_billing_fields(driver):
    """
    Test checkout rejects submission with missing mandatory billing fields.
    
    Validates that:
    - Checkout page loads successfully
    - Error is displayed when attempting to proceed without filling mandatory fields
    - Error message provides guidance about missing fields
    - Mandatory field validation is working
    - Test indicates proper rejection of incomplete billing information
    """
    logger = LoggerFactory.get_logger(__name__)
    
    # Initialize CheckoutFlow
    checkout_flow = CheckoutFlow(driver)
    
    # Call the Flow method - single entry point for this test
    result = checkout_flow.verify_checkout_rejects_missing_mandatory_billing_fields()
    
    # Assertions verifying mandatory field validation
    assert result is not None, "Flow method should return a result dictionary"
    
    assert result.get('test_case_title') == 'Verify Checkout rejects missing mandatory billing fields', \
        "Test case title should be correctly set"
    
    assert result.get('page_loaded') is True, \
        "Checkout page should load successfully"
    
    assert result.get('error_displayed') is True, \
        "Error message should be displayed when mandatory billing fields are missing"
    
    assert result.get('error_message') is not None, \
        "Error message content should be available to inform user about missing mandatory fields"
    
    # Verify error message contains helpful information
    error_msg = result.get('error_message', '')
    assert len(error_msg) > 0, \
        "Error message should not be empty - should contain specific field validation information"
    
    assert result.get('mandatory_fields_validated') is True, \
        "Mandatory field validation should be working (error displayed for incomplete form)"
    
    assert result.get('test_passed') is True, \
        "Test should pass - checkout should properly reject incomplete billing form"
    
    assert result.get('test_failure_reason') is None, \
        "There should be no failure reason when validation is working correctly"
    
    # Log test completion with validation details
    logger.info("✓ Test PASSED: Checkout properly validates and rejects missing mandatory billing fields")
    print("\n" + "="*80)
    print("TEST RESULT: PASSED")
    print("="*80)
    print(f"Test Case: {result.get('test_case_title')}")
    print(f"Page Loaded: {result.get('page_loaded')}")
    print(f"Error Displayed: {result.get('error_displayed')}")
    print(f"Error Message: {result.get('error_message')}")
    print(f"Mandatory Fields Validated: {result.get('mandatory_fields_validated')}")
    print(f"Validation Working: {result.get('test_passed')}")
    print("Validation Result: Missing mandatory billing fields properly rejected")
    print("="*80 + "\n")
