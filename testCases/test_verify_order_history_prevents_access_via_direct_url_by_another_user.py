import pytest
from flows.orderHistoryFlow import OrderHistoryFlow


@pytest.mark.ui
@pytest.mark.regression
class TestVerifyOrderHistoryPreventsAccessViaDirectUrlByAnotherUser:
    """
    Test suite for verifying Order History access control security.
    
    Tests that the Order History page prevents unauthorized cross-user access
    through direct URL manipulation or direct page access.
    """

    def test_verify_order_history_prevents_access_via_direct_url_by_another_user(self, driver, authenticated_user):
        """
        Test: Verify Order History prevents access via direct URL by another user.
        
        Verifies that:
        - Order History page is accessible via valid URL for authenticated user
        - Orders displayed belong only to the current user
        - Direct URL access by unauthorized users is prevented
        - No cross-user order visibility vulnerabilities exist
        
        Args:
            driver: Selenium WebDriver fixture
            authenticated_user: Authenticated user fixture ensuring user is logged in
        
        Asserts:
            - Test result is not None
            - Test passes (access control is properly enforced)
            - Page URL is valid
            - Access is restricted to current user only
            - No unauthorized URL access vulnerabilities detected
            - Test failure reason is None when test passes
        """
        # Arrange
        order_history_flow = OrderHistoryFlow(driver)
        
        # Act
        result = order_history_flow.verify_order_history_prevents_access_via_direct_url_by_another_user()
        
        # Assert
        assert result is not None, "Access control validation result should not be None"
        assert result.get('test_passed') is True, \
            f"Order History access control validation failed: {result.get('test_failure_reason')}"
        assert result.get('current_url') is not None, \
            "Current URL should be available"
        assert result.get('valid_page') is True, \
            "Order History page URL should be valid"
        assert result.get('access_restricted') is True, \
            "Order History access should be properly restricted"
        assert result.get('orders_count') is not None, \
            "Orders count should be available in result"
        assert result.get('test_failure_reason') is None, \
            "Test failure reason should be None when access control is properly enforced"
