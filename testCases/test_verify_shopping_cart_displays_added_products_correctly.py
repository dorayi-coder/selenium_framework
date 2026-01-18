import pytest
from flows.shoppingCartFlow import ShoppingCartFlow


@pytest.mark.ui
@pytest.mark.regression
class TestVerifyShoppingCartDisplaysAddedProductsCorrectly:
    """Test: Verify Shopping Cart displays added products correctly."""
    
    def test_verify_shopping_cart_displays_added_products_correctly(self, driver, shopping_cart_with_items):
        """
        Verify Shopping Cart displays added products correctly.
        
        This test verifies:
        1. Shopping cart page loads successfully
        2. Cart item count is retrieved
        3. All product names are visible in cart
        4. All product prices are visible in cart
        5. Number of products matches item count
        6. All products have valid names (non-empty)
        7. All products have valid prices (non-empty)
        8. Overall validation passes with correct display
        
        Args:
            driver: Selenium WebDriver fixture
            shopping_cart_with_items: Fixture providing shopping cart with products
        """
        # Arrange
        cart_flow = ShoppingCartFlow(driver)
        
        # Act
        result = cart_flow.verify_shopping_cart_displays_added_products_correctly()
        
        # Assert
        assert result is not None
        assert result.get('test_passed') is True
        assert result.get('test_case_title') is not None
        assert isinstance(result.get('total_products'), int)
        assert result.get('total_products') > 0
        assert isinstance(result.get('products_with_names'), int)
        assert result.get('products_with_names') > 0
        assert isinstance(result.get('products_with_prices'), int)
        assert result.get('products_with_prices') > 0
        assert result.get('all_names_present') is True
        assert result.get('all_prices_present') is True
        assert result.get('products_with_names') == result.get('total_products')
        assert result.get('products_with_prices') == result.get('total_products')
        assert result.get('test_failure_reason') is None
