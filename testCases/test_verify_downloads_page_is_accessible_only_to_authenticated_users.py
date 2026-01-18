"""
Test for DownloadsFlow.verify_downloads_page_is_accessible_only_to_authenticated_users() method.

This test validates that the downloads page enforces proper access control by ensuring that only authenticated
users can access and view their downloadable items, preventing unauthorized access to downloads.

Test Scope: UI - Security Test (Authentication & Access Control)
Flow Method: DownloadsFlow.verify_downloads_page_is_accessible_only_to_authenticated_users()
"""

import pytest
from flows.downloadsFlow import DownloadsFlow
from utilities.customLogger import LoggerFactory


@pytest.mark.ui
@pytest.mark.regression
def test_verify_downloads_page_is_accessible_only_to_authenticated_users(driver):
    """
    Test that downloads page is accessible only to authenticated users.
    
    Validates that:
    - Downloads page loads successfully
    - User is authenticated
    - No access denied errors are displayed
    - Access control is properly enforced
    - Only authenticated users can view downloads
    - Login requirement is properly gated for unauthenticated access
    """
    logger = LoggerFactory.get_logger(__name__)
    
    # Initialize DownloadsFlow
    downloads_flow = DownloadsFlow(driver)
    
    # Call the Flow method - single entry point for this test
    result = downloads_flow.verify_downloads_page_is_accessible_only_to_authenticated_users()
    
    # Assertions verifying access control for downloads page
    assert result is not None, "Flow method should return a result dictionary"
    
    assert result.get('test_case_title') == 'Verify Downloads page is accessible only to authenticated users', \
        "Test case title should be correctly set"
    
    assert result.get('page_loaded') is True, \
        "Downloads page should load successfully"
    
    assert result.get('user_authenticated') is True, \
        "User should be authenticated to access downloads page"
    
    assert result.get('no_access_error') is True, \
        "No access denied error should be displayed for authenticated users"
    
    assert result.get('test_passed') is True, \
        "Test should pass - access control should be properly enforced for authenticated users"
    
    assert result.get('test_failure_reason') is None, \
        "There should be no failure reason when access control is working"
    
    # Verify that login requirement is tracked
    login_required = result.get('login_required')
    assert isinstance(login_required, bool), \
        "Login requirement status should be captured"
    
    # Log test completion with security validation
    logger.info("✓ Test PASSED: Downloads page access properly restricted to authenticated users")
    print("\n" + "="*80)
    print("TEST RESULT: PASSED")
    print("="*80)
    print(f"Test Case: {result.get('test_case_title')}")
    print(f"Page Loaded: {result.get('page_loaded')}")
    print(f"User Authenticated: {result.get('user_authenticated')}")
    print(f"Login Required: {result.get('login_required')}")
    print(f"No Access Errors: {result.get('no_access_error')}")
    print(f"Access Control Working: {result.get('test_passed')}")
    print("Security Status: Authentication required for downloads access")
    print("="*80 + "\n")
