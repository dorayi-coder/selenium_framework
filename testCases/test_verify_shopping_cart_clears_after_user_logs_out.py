import pytest
from flows.shoppingCartFlow import ShoppingCartFlow


@pytest.mark.ui
@pytest.mark.regression
class TestVerifyShoppingCartClearsAfterUserLogsOut:
    """Test: Verify Shopping Cart clears after user logs out."""
    
    def test_verify_shopping_cart_clears_after_user_logs_out(self, driver, authenticated_user):
        """
        Verify Shopping Cart clears after user logs out.
        
        Tests that cart is emptied when user logs out from the application.
        
        Verification Points:
        - Initial cart count is captured
        - Cart is empty after logout
        - Test passes when cart is cleared
        - Failure reason is None on success
        
        Args:
            driver: Selenium WebDriver fixture
            authenticated_user: Fixture providing authenticated user context
        """
        # Arrange
        cart_flow = ShoppingCartFlow(driver)
        
        # Act
        result = cart_flow.verify_shopping_cart_clears_after_user_logs_out()
        
        # Assert
        assert result is not None
        assert result.get('test_passed') is True
        assert result.get('cart_empty_after_logout') is True
        assert result.get('initial_cart_count') >= 0
        assert result.get('test_case_title') is not None
        assert result.get('test_failure_reason') is None
