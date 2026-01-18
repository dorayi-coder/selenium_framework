import pytest
from flows.shoppingCartFlow import ShoppingCartFlow


@pytest.mark.ui
@pytest.mark.regression
class TestVerifyShoppingCartApplesProductPriceCorrectly:
    """Test: Verify Shopping Cart applies product price correctly."""
    
    def test_verify_shopping_cart_applies_product_price_correctly(self, driver, shopping_cart_with_items):
        """
        Verify Shopping Cart applies product price correctly.
        
        Tests that product prices are displayed and total is calculated correctly.
        
        Verification Points:
        - All products have prices displayed
        - Subtotal is calculated correctly
        - Total is calculated correctly
        - Prices are valid (not None/empty)
        
        Args:
            driver: Selenium WebDriver fixture
            shopping_cart_with_items: Fixture providing cart with products
        """
        # Arrange
        cart_flow = ShoppingCartFlow(driver)
        
        # Act
        result = cart_flow.verify_shopping_cart_applies_product_price_correctly()
        
        # Assert
        assert result is not None
        assert result.get('test_passed') is True
        assert result.get('prices_valid') is True
        assert result.get('totals_valid') is True
        assert result.get('total_products') > 0
        assert result.get('products_with_prices') == result.get('total_products')
        assert result.get('subtotal') is not None
        assert result.get('total') is not None
        assert result.get('test_case_title') is not None
        assert result.get('test_failure_reason') is None
