import pytest
from flows.orderHistoryFlow import OrderHistoryFlow


@pytest.mark.ui
@pytest.mark.regression
class TestVerifyOrderHistoryPageIsAccessibleOnlyToAuthenticatedUsers:
    """
    Test suite for verifying Order History page authentication access control.
    
    Tests that the Order History page requires user authentication and
    is not accessible to unauthenticated users.
    """

    def test_verify_order_history_page_is_accessible_only_to_authenticated_users(self, driver, authenticated_user):
        """
        Test: Verify Order History page is accessible only to authenticated users.
        
        Verifies that:
        - Order History page loads only for authenticated users
        - User is not redirected to login page
        - Page displays authenticated user content
        - Unauthenticated access is prevented
        
        Args:
            driver: Selenium WebDriver fixture
            authenticated_user: Authenticated user fixture ensuring user is logged in
        
        Asserts:
            - Page loads successfully (user is authenticated)
            - User is not redirected to login page
            - User is recognized as authenticated
            - Access control test passes
        """
        # Arrange
        order_history_flow = OrderHistoryFlow(driver)
        
        # Act
        result = order_history_flow.verify_order_history_page_is_accessible_only_to_authenticated_users()
        
        # Assert
        assert result is not None, "Authentication validation result should not be None"
        assert result.get('test_passed') is True, \
            f"Order History authentication validation failed: {result.get('test_failure_reason')}"
        assert result.get('page_loaded') is True, \
            "Order History page should load for authenticated user"
        assert result.get('authenticated') is True, \
            "User should be recognized as authenticated"
        assert result.get('on_login_page') is False, \
            "User should not be redirected to login page"
        assert result.get('current_url') is not None, \
            "Current URL should be available"
