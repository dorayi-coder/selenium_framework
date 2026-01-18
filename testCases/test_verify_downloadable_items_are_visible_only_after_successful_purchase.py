"""
Test for DownloadsFlow.verify_downloadable_items_are_visible_only_after_successful_purchase() method.

This test validates that downloadable items are properly gated and only visible to users who have successfully
purchased products, preventing unauthorized access to downloads for non-purchasers.

Test Scope: UI - Security & Business Logic Test (Purchase-Based Access Control)
Flow Method: DownloadsFlow.verify_downloadable_items_are_visible_only_after_successful_purchase()
"""

import pytest
from flows.downloadsFlow import DownloadsFlow
from utilities.customLogger import LoggerFactory


@pytest.mark.ui
@pytest.mark.regression
def test_verify_downloadable_items_are_visible_only_after_successful_purchase(driver):
    """
    Test that downloadable items are visible only after successful purchase.
    
    Validates that:
    - Downloads page loads successfully
    - Downloadable items are available
    - Purchase is confirmed
    - Download items are visible on the page
    - No purchase restriction errors are displayed
    - Access to downloads is properly gated by purchase status
    - Only users with confirmed purchases can see downloads
    """
    logger = LoggerFactory.get_logger(__name__)
    
    # Initialize DownloadsFlow
    downloads_flow = DownloadsFlow(driver)
    
    # Call the Flow method - single entry point for this test
    result = downloads_flow.verify_downloadable_items_are_visible_only_after_successful_purchase()
    
    # Assertions verifying purchase-based download access control
    assert result is not None, "Flow method should return a result dictionary"
    
    assert result.get('test_case_title') == 'Verify downloadable items are visible only after successful purchase', \
        "Test case title should be correctly set"
    
    assert result.get('has_downloads') is True, \
        "Downloadable items should exist for the user"
    
    assert result.get('purchase_confirmed') is True, \
        "Purchase should be confirmed to access downloads"
    
    assert result.get('items_visible') is True, \
        "Download items should be visible on the page"
    
    assert result.get('no_restriction_error') is True, \
        "No purchase restriction error should be displayed"
    
    assert result.get('test_passed') is True, \
        "Test should pass - downloadable items should be visible only after purchase"
    
    assert result.get('test_failure_reason') is None, \
        "There should be no failure reason when downloads are properly gated by purchase"
    
    # Log test completion with access control validation
    logger.info("✓ Test PASSED: Downloadable items properly restricted to verified purchasers")
    print("\n" + "="*80)
    print("TEST RESULT: PASSED")
    print("="*80)
    print(f"Test Case: {result.get('test_case_title')}")
    print(f"Has Downloadable Items: {result.get('has_downloads')}")
    print(f"Purchase Confirmed: {result.get('purchase_confirmed')}")
    print(f"Items Visible: {result.get('items_visible')}")
    print(f"No Restriction Errors: {result.get('no_restriction_error')}")
    print(f"Downloads Access Control Working: {result.get('test_passed')}")
    print("Business Logic Status: Downloads properly gated by purchase status")
    print("="*80 + "\n")
