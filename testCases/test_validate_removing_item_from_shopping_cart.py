import pytest
from flows.shoppingCartFlow import ShoppingCartFlow


@pytest.mark.ui
@pytest.mark.regression
class TestValidateRemovingItemFromShoppingCart:
    """Test: Validate removing the item from the shopping cart."""
    
    def test_validate_removing_item_from_shopping_cart(self, driver, shopping_cart_with_items):
        """
        Validate removing an item from the shopping cart.
        
        This test verifies:
        1. Shopping cart page loads successfully
        2. Initial cart item count is retrieved
        3. Product at index 0 is removed from cart
        4. Cart item count is updated after removal
        5. Item count decreased by exactly one
        6. Removal operation completes successfully
        7. Cart state is updated immediately after removal
        
        Args:
            driver: Selenium WebDriver fixture
            shopping_cart_with_items: Fixture providing shopping cart with products
        """
        # Arrange
        cart_flow = ShoppingCartFlow(driver)
        product_index = 0
        
        # Act
        result = cart_flow.validate_removing_item_from_shopping_cart(product_index)
        
        # Assert
        assert result is not None
        assert result.get('test_passed') is True
        assert result.get('test_case_title') is not None
        assert result.get('product_index') == product_index
        assert isinstance(result.get('initial_cart_count'), int)
        assert result.get('initial_cart_count') > 0
        assert isinstance(result.get('updated_cart_count'), int)
        assert result.get('updated_cart_count') >= 0
        assert result.get('item_removed') is True
        assert result.get('count_decreased_by_one') is True
        assert result.get('updated_cart_count') == (result.get('initial_cart_count') - 1)
        assert result.get('test_failure_reason') is None
