import pytest
from flows.shoppingCartFlow import ShoppingCartFlow


@pytest.mark.ui
@pytest.mark.regression
class TestVerifyShoppingCartUpdatesTotalsAfterProductRemoval:
    """Test: Verify Shopping Cart updates totals after product removal."""
    
    def test_verify_shopping_cart_updates_totals_after_product_removal(self, driver, shopping_cart_with_items):
        """
        Verify Shopping Cart updates totals after product removal.
        
        Tests that cart totals (subtotal and total) decrease after removing a product.
        
        Verification Points:
        - Initial subtotal and total are captured
        - Product is removed from cart
        - Updated subtotal and total are less than initial values
        - Both totals decrease correctly
        
        Args:
            driver: Selenium WebDriver fixture
            shopping_cart_with_items: Fixture providing cart with products
        """
        # Arrange
        cart_flow = ShoppingCartFlow(driver)
        
        # Act
        result = cart_flow.verify_shopping_cart_updates_totals_after_product_removal()
        
        # Assert
        assert result is not None
        assert result.get('test_passed') is True
        assert result.get('subtotal_decreased') is True
        assert result.get('total_decreased') is True
        assert result.get('initial_subtotal') is not None
        assert result.get('updated_subtotal') is not None
        assert result.get('initial_total') is not None
        assert result.get('updated_total') is not None
        assert result.get('product_index') >= 0
        assert result.get('test_case_title') is not None
        assert result.get('test_failure_reason') is None
