"""
Test for NewsletterFlow.verify_re_subscription_works_after_unsubscribe() method.

This test validates that users can successfully re-subscribe to the newsletter after unsubscribing,
ensuring that the subscription system properly handles the lifecycle of subscription state changes
and allows users to rejoin the newsletter at any time.

Test Scope: UI - Re-subscription After Unsubscribe Test
Flow Method: NewsletterFlow.verify_re_subscription_works_after_unsubscribe()
"""

import pytest
from flows.newsletterFlow import NewsletterFlow
from utilities.customLogger import LoggerFactory


@pytest.mark.ui
@pytest.mark.regression
def test_verify_re_subscription_works_after_unsubscribe(driver):
    """
    Test that re-subscription works after unsubscribe.
    
    Validates that:
    - Newsletter page loads successfully
    - Initial subscription to newsletter succeeds
    - Unsubscribe action completes successfully
    - Re-subscription to newsletter succeeds
    - Email can be reused for subscription after unsubscribe
    - Subscription lifecycle is properly managed
    - Test passes indicating complete subscription flow works
    - No failure reason when all steps complete successfully
    """
    logger = LoggerFactory.get_logger(__name__)
    
    # Initialize NewsletterFlow
    newsletter_flow = NewsletterFlow(driver)
    
    # Call the Flow method - single entry point for this test
    result = newsletter_flow.verify_re_subscription_works_after_unsubscribe()
    
    # Assertions verifying re-subscription after unsubscribe workflow
    assert result is not None, "Flow method should return a result dictionary"
    
    assert result.get('test_case_title') == "Verify re-subscription works after unsubscribe", \
        "Test case title should be correctly set"
    
    assert result.get('initial_subscription_success') is not None, \
        "Initial subscription success flag should be set"
    
    assert result.get('initial_subscription_success') is True, \
        "Initial subscription should succeed"
    
    assert result.get('unsubscribe_success') is not None, \
        "Unsubscribe success flag should be set"
    
    assert result.get('unsubscribe_success') is True, \
        "Unsubscribe operation should succeed"
    
    assert result.get('re_subscription_success') is not None, \
        "Re-subscription success flag should be set"
    
    assert result.get('re_subscription_success') is True, \
        "Re-subscription should succeed after unsubscribe"
    
    assert result.get('test_passed') is True, \
        "Test should pass - re-subscription workflow should work correctly"
    
    assert result.get('test_failure_reason') is None, \
        "There should be no failure reason when all subscription lifecycle steps succeed"
    
    # Verify consistency of subscription lifecycle flags
    subscription_lifecycle_complete = (
        result.get('initial_subscription_success') and 
        result.get('unsubscribe_success') and 
        result.get('re_subscription_success')
    )
    assert subscription_lifecycle_complete == result.get('test_passed'), \
        "Test passed status should reflect completion of all subscription lifecycle steps"
    
    # Verify all steps are executed in order
    assert result.get('initial_subscription_success') is True, \
        "First subscription attempt must succeed before unsubscribe"
    
    assert result.get('unsubscribe_success') is True, \
        "Unsubscribe must succeed before re-subscription"
    
    # Log test completion with subscription lifecycle details
    logger.info(f"✓ Test PASSED: Re-subscription works correctly after unsubscribe")
    print("\n" + "="*80)
    print("TEST RESULT: PASSED")
    print("="*80)
    print(f"Test Case: {result.get('test_case_title')}")
    print(f"Initial Subscription: {result.get('initial_subscription_success')}")
    print(f"Unsubscribe Operation: {result.get('unsubscribe_success')}")
    print(f"Re-subscription: {result.get('re_subscription_success')}")
    print(f"Subscription Lifecycle: Complete and working correctly")
    print(f"User Capability: Can unsubscribe and rejoin newsletter anytime")
    print("="*80 + "\n")
