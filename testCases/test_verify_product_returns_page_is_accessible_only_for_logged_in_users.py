import pytest
from flows.productReturnsFlow import ProductReturnsFlow


@pytest.mark.ui
@pytest.mark.regression
class TestVerifyProductReturnsPageIsAccessibleOnlyForLoggedInUsers:
    """Test: Verify product returns page is accessible only for logged-in users."""
    
    def test_verify_product_returns_page_is_accessible_only_for_logged_in_users(self, driver, authenticated_user):
        """
        Verify that the product returns page is accessible only to authenticated/logged-in users.
        
        This test validates that:
        - Returns page loads successfully
        - User must be authenticated to access the page
        - No access denied errors are displayed for logged-in users
        - Access control is properly enforced
        - Logged-in users can access the returns page
        - Page is not accessible to unauthenticated users
        
        Args:
            driver: Selenium WebDriver instance from pytest fixture
            authenticated_user: Authenticated user context fixture
        
        Assert:
            - result dictionary is not None
            - test_passed is True
            - page_loaded is True
            - user_authenticated is True
            - no_access_error is True
            - test_failure_reason is None
        """
        # Arrange
        product_returns_flow = ProductReturnsFlow(driver)
        
        # Act
        result = product_returns_flow.verify_product_returns_page_is_accessible_only_for_logged_in_users()
        
        # Assert
        assert result is not None
        assert result.get('test_passed') is True
        assert result.get('page_loaded') is True
        assert result.get('user_authenticated') is True
        assert result.get('no_access_error') is True
        assert result.get('test_failure_reason') is None
