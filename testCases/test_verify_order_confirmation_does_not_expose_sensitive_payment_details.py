"""
Test for OrderConfirmationFlow.verify_order_confirmation_does_not_expose_sensitive_payment_details() method.

This test validates that the Order Confirmation page does not expose sensitive payment information
such as full credit card numbers or CVV codes, ensuring PCI DSS compliance and protecting customer
payment data security.

Test Scope: UI - Payment Security Test
Flow Method: OrderConfirmationFlow.verify_order_confirmation_does_not_expose_sensitive_payment_details()
"""

import pytest
from flows.orderConfirmationFlow import OrderConfirmationFlow
from utilities.customLogger import LoggerFactory


@pytest.mark.ui
@pytest.mark.regression
def test_verify_order_confirmation_does_not_expose_sensitive_payment_details(driver):
    """
    Test that Order Confirmation does not expose sensitive payment details.
    
    Validates that:
    - Order Confirmation page loads successfully
    - Full credit card numbers are NOT visible on page
    - CVV/CVC codes are NOT visible on page
    - Payment method is displayed in masked format
    - Sensitive payment data is properly protected
    - PCI DSS compliance is maintained
    - Customer payment information is secure
    - Test passes indicating proper payment data protection
    - No failure reason when sensitive data is protected
    """
    logger = LoggerFactory.get_logger(__name__)
    
    # Initialize OrderConfirmationFlow
    confirmation_flow = OrderConfirmationFlow(driver)
    
    # Call the Flow method - single entry point for this test
    result = confirmation_flow.verify_order_confirmation_does_not_expose_sensitive_payment_details()
    
    # Assertions verifying payment data security and protection
    assert result is not None, "Flow method should return a result dictionary"
    
    assert result.get('test_case_title') == "Verify Order Confirmation does not expose sensitive payment details", \
        "Test case title should be correctly set"
    
    assert result.get('full_card_number_exposed') is not None, \
        "Full card number exposure flag should be set"
    
    assert result.get('full_card_number_exposed') is False, \
        "Full credit card numbers should NOT be exposed on confirmation page"
    
    assert result.get('cvv_exposed') is not None, \
        "CVV exposure flag should be set"
    
    assert result.get('cvv_exposed') is False, \
        "CVV/CVC codes should NOT be exposed on confirmation page"
    
    assert result.get('payment_method_masked') is not None, \
        "Payment method masking flag should be set"
    
    assert result.get('payment_method_masked') is True, \
        "Payment method should be displayed in masked format"
    
    assert result.get('sensitive_data_protected') is not None, \
        "Sensitive data protection flag should be set"
    
    assert result.get('sensitive_data_protected') is True, \
        "Sensitive payment data should be properly protected"
    
    assert result.get('test_passed') is True, \
        "Test should pass - sensitive payment details should not be exposed"
    
    assert result.get('test_failure_reason') is None, \
        "There should be no failure reason when payment data is properly protected"
    
    # Verify consistency of security flags
    security_verified = not result.get('full_card_number_exposed') and not result.get('cvv_exposed')
    assert security_verified, \
        "Payment security should be verified - no sensitive data exposed"
    
    # Verify test result consistency
    assert result.get('sensitive_data_protected') == result.get('test_passed'), \
        "Sensitive data protection status should match test passed result"
    
    # Log test completion with security verification details
    logger.info(f"✓ Test PASSED: Payment data properly protected on Order Confirmation page")
    print("\n" + "="*80)
    print("TEST RESULT: PASSED")
    print("="*80)
    print(f"Test Case: {result.get('test_case_title')}")
    print(f"Full Card Number Exposed: {result.get('full_card_number_exposed')}")
    print(f"CVV Exposed: {result.get('cvv_exposed')}")
    print(f"Payment Method Masked: {result.get('payment_method_masked')}")
    print(f"Sensitive Data Protected: {result.get('sensitive_data_protected')}")
    print(f"Security Status: PCI DSS Compliance maintained")
    print(f"Customer Data Protection: Payment information properly secured")
    print("="*80 + "\n")
