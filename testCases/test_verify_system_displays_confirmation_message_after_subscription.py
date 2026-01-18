"""
Test for NewsletterFlow.verify_system_displays_confirmation_message_after_subscription() method.

This test validates that the system displays a confirmation message to users after they successfully
subscribe to the newsletter, providing clear feedback that their subscription action was completed
successfully.

Test Scope: UI - Subscription Confirmation Message Test
Flow Method: NewsletterFlow.verify_system_displays_confirmation_message_after_subscription()
"""

import pytest
from flows.newsletterFlow import NewsletterFlow
from utilities.customLogger import LoggerFactory


@pytest.mark.ui
@pytest.mark.regression
def test_verify_system_displays_confirmation_message_after_subscription(driver):
    """
    Test that system displays confirmation message after subscription.
    
    Validates that:
    - Newsletter page loads successfully
    - Valid email is used for subscription
    - Email is entered into subscription field
    - Subscription action completes
    - Confirmation message is displayed to user
    - Subscription is marked as successful
    - User receives clear feedback on successful subscription
    - Test passes indicating confirmation message displayed
    - No failure reason when confirmation message shown
    """
    logger = LoggerFactory.get_logger(__name__)
    
    # Initialize NewsletterFlow
    newsletter_flow = NewsletterFlow(driver)
    
    # Call the Flow method - single entry point for this test
    result = newsletter_flow.verify_system_displays_confirmation_message_after_subscription()
    
    # Assertions verifying confirmation message display after subscription
    assert result is not None, "Flow method should return a result dictionary"
    
    assert result.get('test_case_title') == "Verify system displays confirmation message after subscription", \
        "Test case title should be correctly set"
    
    assert result.get('email_entered') is not None, \
        "Email used for subscription should be captured"
    
    email_entered = result.get('email_entered', '')
    assert len(email_entered) > 0, \
        "Email entered should not be empty"
    
    assert '@' in email_entered, \
        "Email entered should contain @ symbol"
    
    assert result.get('confirmation_message_visible') is not None, \
        "Confirmation message visibility flag should be set"
    
    assert result.get('confirmation_message_visible') is True, \
        "Confirmation message should be visible after subscription"
    
    assert result.get('subscription_successful') is not None, \
        "Subscription success flag should be set"
    
    assert result.get('subscription_successful') is True, \
        "Subscription should be marked as successful"
    
    assert result.get('test_passed') is True, \
        "Test should pass - confirmation message should be displayed"
    
    assert result.get('test_failure_reason') is None, \
        "There should be no failure reason when confirmation message is displayed"
    
    # Verify consistency of flags
    assert result.get('confirmation_message_visible') == result.get('subscription_successful'), \
        "Confirmation message and subscription success flags should be consistent"
    
    # Log test completion with subscription confirmation details
    logger.info(f"✓ Test PASSED: System displays confirmation message after subscription for {email_entered}")
    print("\n" + "="*80)
    print("TEST RESULT: PASSED")
    print("="*80)
    print(f"Test Case: {result.get('test_case_title')}")
    print(f"Email Subscribed: {result.get('email_entered')}")
    print(f"Confirmation Message Visible: {result.get('confirmation_message_visible')}")
    print(f"Subscription Successful: {result.get('subscription_successful')}")
    print(f"User Feedback: Clear confirmation message displayed")
    print(f"Subscription Status: Successfully completed with visual confirmation")
    print("="*80 + "\n")
