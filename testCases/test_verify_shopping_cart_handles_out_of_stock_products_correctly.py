import pytest
from flows.shoppingCartFlow import ShoppingCartFlow


@pytest.mark.ui
@pytest.mark.regression
class TestVerifyShoppingCartHandlesOutOfStockProductsCorrectly:
    """Test: Verify shopping cart handles out-of-stock products correctly."""
    
    def test_verify_shopping_cart_handles_out_of_stock_products_correctly(self, driver, shopping_cart_with_items):
        """
        Verify shopping cart handles out-of-stock products correctly.
        
        Tests that cart properly displays out-of-stock status or messages when products become unavailable.
        
        Verification Points:
        - Cart is either empty or error message is displayed for out-of-stock products
        - Out-of-stock handling is confirmed (not processing invalid items)
        - Error message is captured if present
        - Item count reflects correct state
        
        Args:
            driver: Selenium WebDriver fixture
            shopping_cart_with_items: Fixture providing cart with products
        """
        # Arrange
        cart_flow = ShoppingCartFlow(driver)
        
        # Act
        result = cart_flow.verify_shopping_cart_handles_out_of_stock_products_correctly()
        
        # Assert
        assert result is not None
        assert result.get('test_passed') is True
        assert result.get('cart_empty') is True or result.get('error_message_displayed') is True
        assert result.get('item_count') >= 0
        assert result.get('test_case_title') is not None
        assert result.get('test_failure_reason') is None
