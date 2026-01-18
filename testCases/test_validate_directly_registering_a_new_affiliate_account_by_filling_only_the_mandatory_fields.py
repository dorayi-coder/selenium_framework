"""
Test for AffiliateFlow.validate_directly_registering_a_new_affiliate_account_by_filling_only_the_mandatory_fields() method.

This test validates that a new affiliate account can be successfully registered by filling only the mandatory fields
(first name, last name, email, and company) without requiring additional optional information.

Test Scope: UI - Positive Registration Test (Mandatory Fields Only)
Flow Method: AffiliateFlow.validate_directly_registering_a_new_affiliate_account_by_filling_only_the_mandatory_fields()
"""

import pytest
from flows.affiliateFlow import AffiliateFlow
from utilities.customLogger import LoggerFactory


@pytest.mark.ui
@pytest.mark.regression
def test_validate_directly_registering_a_new_affiliate_account_by_filling_only_the_mandatory_fields(driver):
    """
    Test affiliate account registration with only mandatory fields filled.
    
    Validates that:
    - Registration form is accessible
    - Mandatory fields can be filled (first name, last name, email, company)
    - Form submission succeeds without optional fields
    - Success message is displayed
    - Account creation completes successfully with minimal required information
    """
    logger = LoggerFactory.get_logger(__name__)
    
    # Initialize AffiliateFlow
    affiliate_flow = AffiliateFlow(driver)
    
    # Call the Flow method - single entry point for this test
    result = affiliate_flow.validate_directly_registering_a_new_affiliate_account_by_filling_only_the_mandatory_fields()
    
    # Assertions verifying the registration outcome with mandatory fields
    assert result is not None, "Flow method should return a result dictionary"
    
    assert result.get('test_case_title') == 'Validate directly registering a new Affiliate Account by filling only the mandatory fields', \
        "Test case title should be correctly set"
    
    assert result.get('registration_form_visible') is True, \
        "Registration form should be visible and accessible"
    
    assert result.get('firstname_filled') is True, \
        "First name field (mandatory) should be successfully filled"
    
    assert result.get('lastname_filled') is True, \
        "Last name field (mandatory) should be successfully filled"
    
    assert result.get('email_filled') is True, \
        "Email field (mandatory) should be successfully filled"
    
    assert result.get('company_filled') is True, \
        "Company field (mandatory) should be successfully filled"
    
    assert result.get('registration_successful') is True, \
        "Registration form submission should succeed with mandatory fields only"
    
    assert result.get('success_message_visible') is True, \
        "Success message should be displayed after registration with mandatory fields"
    
    assert result.get('test_passed') is True, \
        "Overall test should pass - affiliate account should be created with mandatory fields"
    
    assert result.get('test_failure_reason') is None, \
        "There should be no failure reason when registration succeeds"
    
    # Log test completion
    logger.info("✓ Test PASSED: Affiliate account successfully registered with mandatory fields only")
    print("\n" + "="*80)
    print("TEST RESULT: PASSED")
    print("="*80)
    print(f"Test Case: {result.get('test_case_title')}")
    print(f"Registration Form Visible: {result.get('registration_form_visible')}")
    print(f"Mandatory Fields Filled:")
    print(f"  - First Name: {result.get('firstname_filled')}")
    print(f"  - Last Name: {result.get('lastname_filled')}")
    print(f"  - Email: {result.get('email_filled')}")
    print(f"  - Company: {result.get('company_filled')}")
    print(f"Registration Successful: {result.get('registration_successful')}")
    print(f"Success Message Displayed: {result.get('success_message_visible')}")
    print(f"Optional Fields Not Required: Verified by successful submission with mandatory fields only")
    print("="*80 + "\n")
