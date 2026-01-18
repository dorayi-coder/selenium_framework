"""
Test for AffiliateFlow.validate_directly_registering_a_new_affiliate_account_by_filling_all_the_fields() method.

This test validates that a new affiliate account can be successfully registered by filling all available fields
including company, name, email, phone, address, city, state, zipcode, and country information.

Test Scope: UI - Positive Registration Test
Flow Method: AffiliateFlow.validate_directly_registering_a_new_affiliate_account_by_filling_all_the_fields()
"""

import pytest
from flows.affiliateFlow import AffiliateFlow
from utilities.customLogger import LoggerFactory


@pytest.mark.ui
@pytest.mark.regression
def test_validate_directly_registering_a_new_affiliate_account_by_filling_all_the_fields(driver):
    """
    Test affiliate account registration with all fields filled.
    
    Validates that:
    - Registration form is accessible
    - All required fields can be filled (company, name, email, phone, address, etc.)
    - Form submission succeeds
    - Success message is displayed
    - Account creation completes successfully
    """
    logger = LoggerFactory.get_logger(__name__)
    
    # Initialize AffiliateFlow
    affiliate_flow = AffiliateFlow(driver)
    
    # Call the Flow method - single entry point for this test
    result = affiliate_flow.validate_directly_registering_a_new_affiliate_account_by_filling_all_the_fields()
    
    # Assertions verifying the registration outcome
    assert result is not None, "Flow method should return a result dictionary"
    
    assert result.get('test_case_title') == 'Validate directly registering a new Affiliate Account by filling all the fields', \
        "Test case title should be correctly set"
    
    assert result.get('registration_form_visible') is True, \
        "Registration form should be visible and accessible"
    
    assert result.get('company_field_filled') is True, \
        "Company field should be successfully filled"
    
    assert result.get('firstname_filled') is True, \
        "First name field should be successfully filled"
    
    assert result.get('lastname_filled') is True, \
        "Last name field should be successfully filled"
    
    assert result.get('email_filled') is True, \
        "Email field should be successfully filled"
    
    assert result.get('phone_filled') is True, \
        "Phone field should be successfully filled"
    
    assert result.get('address_filled') is True, \
        "Address field should be successfully filled"
    
    assert result.get('city_filled') is True, \
        "City field should be successfully filled"
    
    assert result.get('state_filled') is True, \
        "State field should be successfully filled"
    
    assert result.get('zipcode_filled') is True, \
        "Zipcode field should be successfully filled"
    
    assert result.get('country_filled') is True, \
        "Country field should be successfully filled"
    
    assert result.get('registration_successful') is True, \
        "Registration form submission should succeed"
    
    assert result.get('success_message_visible') is True, \
        "Success message should be displayed after registration"
    
    assert result.get('test_passed') is True, \
        "Overall test should pass - affiliate account should be created"
    
    assert result.get('test_failure_reason') is None, \
        "There should be no failure reason when registration succeeds"
    
    # Log test completion
    logger.info("✓ Test PASSED: Affiliate account successfully registered with all fields filled")
    print("\n" + "="*80)
    print("TEST RESULT: PASSED")
    print("="*80)
    print(f"Test Case: {result.get('test_case_title')}")
    print(f"Registration Form Visible: {result.get('registration_form_visible')}")
    print(f"All Fields Filled: Company={result.get('company_field_filled')}, "
          f"FirstName={result.get('firstname_filled')}, LastName={result.get('lastname_filled')}, "
          f"Email={result.get('email_filled')}, Phone={result.get('phone_filled')}")
    print(f"Address Information: Address={result.get('address_filled')}, City={result.get('city_filled')}, "
          f"State={result.get('state_filled')}, Zipcode={result.get('zipcode_filled')}, Country={result.get('country_filled')}")
    print(f"Registration Successful: {result.get('registration_successful')}")
    print(f"Success Message Displayed: {result.get('success_message_visible')}")
    print("="*80 + "\n")
