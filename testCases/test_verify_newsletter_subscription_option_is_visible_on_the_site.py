"""
Test for NewsletterFlow.verify_newsletter_subscription_option_is_visible_on_the_site() method.

This test validates that the newsletter subscription option (heading, email input, and subscribe button)
is visible and accessible on the website, ensuring users can easily discover and access the newsletter
subscription functionality.

Test Scope: UI - Newsletter Visibility Test
Flow Method: NewsletterFlow.verify_newsletter_subscription_option_is_visible_on_the_site()
"""

import pytest
from flows.newsletterFlow import NewsletterFlow
from utilities.customLogger import LoggerFactory


@pytest.mark.ui
@pytest.mark.regression
def test_verify_newsletter_subscription_option_is_visible_on_the_site(driver):
    """
    Test that newsletter subscription option is visible on the site.
    
    Validates that:
    - Newsletter page loads successfully
    - Newsletter heading is visible
    - Email input field is visible
    - Subscribe button is visible
    - All required components are present and visible
    - Subscription option is fully accessible to users
    - Test passes indicating visibility compliance
    - No failure reason when all components are visible
    """
    logger = LoggerFactory.get_logger(__name__)
    
    # Initialize NewsletterFlow
    newsletter_flow = NewsletterFlow(driver)
    
    # Call the Flow method - single entry point for this test
    result = newsletter_flow.verify_newsletter_subscription_option_is_visible_on_the_site()
    
    # Assertions verifying newsletter subscription option visibility
    assert result is not None, "Flow method should return a result dictionary"
    
    assert result.get('test_case_title') == "Verify Newsletter subscription option is visible on the site", \
        "Test case title should be correctly set"
    
    assert result.get('newsletter_heading_visible') is not None, \
        "Newsletter heading visibility flag should be set"
    
    assert result.get('newsletter_heading_visible') is True, \
        "Newsletter heading should be visible on the site"
    
    assert result.get('email_input_visible') is not None, \
        "Email input visibility flag should be set"
    
    assert result.get('email_input_visible') is True, \
        "Email input field should be visible on the site"
    
    assert result.get('subscribe_button_visible') is not None, \
        "Subscribe button visibility flag should be set"
    
    assert result.get('subscribe_button_visible') is True, \
        "Subscribe button should be visible on the site"
    
    assert result.get('test_passed') is True, \
        "Test should pass - all newsletter subscription components should be visible"
    
    assert result.get('test_failure_reason') is None, \
        "There should be no failure reason when all components are visible"
    
    # Verify consistency of visibility flags
    all_components_visible = (
        result.get('newsletter_heading_visible') and 
        result.get('email_input_visible') and 
        result.get('subscribe_button_visible')
    )
    assert all_components_visible == result.get('test_passed'), \
        "Test passed status should reflect visibility of all components"
    
    # Log test completion with visibility details
    logger.info(f"✓ Test PASSED: Newsletter subscription option is visible on the site")
    print("\n" + "="*80)
    print("TEST RESULT: PASSED")
    print("="*80)
    print(f"Test Case: {result.get('test_case_title')}")
    print(f"Newsletter Heading Visible: {result.get('newsletter_heading_visible')}")
    print(f"Email Input Field Visible: {result.get('email_input_visible')}")
    print(f"Subscribe Button Visible: {result.get('subscribe_button_visible')}")
    print(f"Newsletter Subscription Option: Fully visible and accessible")
    print(f"User Discoverability: All subscription components present")
    print("="*80 + "\n")
