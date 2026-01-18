"""
Test for MyAccountFlow.verify_my_account_fields_are_accessible_using_keyboard_navigation() method.

This test validates that all form fields on the My Account page are accessible via keyboard navigation,
ensuring compliance with accessibility standards and allowing users with keyboard-only input to navigate
and interact with all account management features.

Test Scope: UI - Keyboard Accessibility Test
Flow Method: MyAccountFlow.verify_my_account_fields_are_accessible_using_keyboard_navigation()
"""

import pytest
from flows.myAccountFlow import MyAccountFlow
from utilities.customLogger import LoggerFactory


@pytest.mark.ui
@pytest.mark.regression
def test_verify_my_account_fields_are_accessible_using_keyboard_navigation(driver):
    """
    Test that My Account fields are accessible using keyboard navigation.
    
    Validates that:
    - My Account page loads successfully
    - Keyboard navigation (Tab key) works on form fields
    - Fields can be traversed using keyboard
    - Navigation focus changes between elements
    - Accessibility compliance is met
    - Test passes indicating keyboard navigation is functional
    - No failure reason when navigation works correctly
    """
    logger = LoggerFactory.get_logger(__name__)
    
    # Initialize MyAccountFlow
    account_flow = MyAccountFlow(driver)
    
    # Call the Flow method - single entry point for this test
    result = account_flow.verify_my_account_fields_are_accessible_using_keyboard_navigation()
    
    # Assertions verifying keyboard accessibility on My Account page
    assert result is not None, "Flow method should return a result dictionary"
    
    assert result.get('test_case_title') == "Verify 'My Account' fields are accessible using keyboard navigation", \
        "Test case title should be correctly set"
    
    assert result.get('keyboard_navigation_works') is not None, \
        "Keyboard navigation flag should be set"
    
    assert isinstance(result.get('keyboard_navigation_works'), bool), \
        "Keyboard navigation flag should be a boolean value"
    
    assert result.get('fields_traversable') is not None, \
        "Fields traversable flag should be set"
    
    assert isinstance(result.get('fields_traversable'), bool), \
        "Fields traversable flag should be a boolean value"
    
    assert result.get('keyboard_navigation_works') is True, \
        "Keyboard navigation should work on form fields"
    
    assert result.get('fields_traversable') is True, \
        "Form fields should be traversable via keyboard"
    
    assert result.get('test_passed') is True, \
        "Test should pass - keyboard navigation should be accessible"
    
    assert result.get('test_failure_reason') is None, \
        "There should be no failure reason when keyboard navigation works correctly"
    
    # Verify consistency between related flags
    assert result.get('keyboard_navigation_works') == result.get('test_passed'), \
        "Keyboard navigation works flag should match test passed result"
    
    assert result.get('fields_traversable') == result.get('test_passed'), \
        "Fields traversable flag should match test passed result"
    
    # Log test completion with accessibility details
    logger.info(f"✓ Test PASSED: My Account fields are accessible via keyboard navigation")
    print("\n" + "="*80)
    print("TEST RESULT: PASSED")
    print("="*80)
    print(f"Test Case: {result.get('test_case_title')}")
    print(f"Keyboard Navigation Works: {result.get('keyboard_navigation_works')}")
    print(f"Fields Traversable: {result.get('fields_traversable')}")
    print(f"Accessibility Compliant: {result.get('test_passed')}")
    print(f"Keyboard Navigation Status: Fully functional and accessible")
    print("Accessibility Standard: WCAG 2.1 Level AA - Keyboard Accessibility")
    print("="*80 + "\n")
