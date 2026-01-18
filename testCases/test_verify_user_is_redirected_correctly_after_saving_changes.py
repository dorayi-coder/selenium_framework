"""
Test for MyAccountFlow.verify_user_is_redirected_correctly_after_saving_changes() method.

This test validates that users are properly redirected after saving changes on the My Account page,
ensuring correct page navigation and state management during account update operations.

Test Scope: UI - Post-Save Redirect Validation Test
Flow Method: MyAccountFlow.verify_user_is_redirected_correctly_after_saving_changes()
"""

import pytest
from flows.myAccountFlow import MyAccountFlow
from utilities.customLogger import LoggerFactory


@pytest.mark.ui
@pytest.mark.regression
def test_verify_user_is_redirected_correctly_after_saving_changes(driver):
    """
    Test that user is redirected correctly after saving changes.
    
    Validates that:
    - My Account page loads successfully
    - URL is captured before save operation
    - Save changes action completes
    - URL is captured after save operation
    - Redirect verification indicates page navigation occurred
    - Redirect flag is properly set
    - Test passes indicating successful redirect
    - URLs differ or page reloaded successfully
    - No failure reason on successful redirect
    """
    logger = LoggerFactory.get_logger(__name__)
    
    # Initialize MyAccountFlow
    account_flow = MyAccountFlow(driver)
    
    # Call the Flow method - single entry point for this test
    result = account_flow.verify_user_is_redirected_correctly_after_saving_changes()
    
    # Assertions verifying post-save redirect behavior
    assert result is not None, "Flow method should return a result dictionary"
    
    assert result.get('test_case_title') == "Verify user is redirected correctly after saving changes", \
        "Test case title should be correctly set"
    
    assert result.get('url_before') is not None, \
        "URL before save operation should be captured"
    
    url_before = result.get('url_before', '')
    assert len(url_before) > 0, \
        "URL before save should not be empty"
    
    assert result.get('url_after') is not None, \
        "URL after save operation should be captured"
    
    url_after = result.get('url_after', '')
    assert len(url_after) > 0, \
        "URL after save should not be empty"
    
    assert result.get('redirect_occurred') is not None, \
        "Redirect occurrence flag should be set"
    
    assert result.get('redirect_occurred') is True, \
        "Redirect should have occurred after saving changes"
    
    assert result.get('test_passed') is True, \
        "Test should pass - user should be redirected after save operation"
    
    assert result.get('test_failure_reason') is None, \
        "There should be no failure reason when redirect occurs successfully"
    
    # Verify URLs changed or page was properly reloaded
    urls_changed = url_before != url_after
    assert urls_changed, \
        "URL should change after save operation OR page should reload with new content"
    
    # Log test completion with redirect details
    logger.info(f"✓ Test PASSED: User redirected correctly after saving changes")
    print("\n" + "="*80)
    print("TEST RESULT: PASSED")
    print("="*80)
    print(f"Test Case: {result.get('test_case_title')}")
    print(f"URL Before Save: {result.get('url_before')}")
    print(f"URL After Save: {result.get('url_after')}")
    print(f"Redirect Occurred: {result.get('redirect_occurred')}")
    print(f"URLs Changed: {urls_changed}")
    print(f"Redirect Validation: Successful - Page navigation working correctly")
    print("="*80 + "\n")
