import pytest
from flows.shoppingCartFlow import ShoppingCartFlow


@pytest.mark.ui
@pytest.mark.regression
class TestVerifyShoppingCartRejectZeroQuantityInput:
    """Test: Verify shopping cart reject zero quantity input."""
    
    def test_verify_shopping_cart_reject_zero_quantity_input(self, driver, shopping_cart_with_items):
        """
        Verify shopping cart reject zero quantity input.
        
        Tests that setting product quantity to zero is rejected with error message.
        
        Verification Points:
        - Error message is displayed when attempting zero quantity
        - Error message text is not None
        - Quantity rejection is confirmed
        
        Args:
            driver: Selenium WebDriver fixture
            shopping_cart_with_items: Fixture providing cart with products
        """
        # Arrange
        cart_flow = ShoppingCartFlow(driver)
        
        # Act
        result = cart_flow.verify_shopping_cart_reject_zero_quantity_input()
        
        # Assert
        assert result is not None
        assert result.get('test_passed') is True
        assert result.get('error_message_displayed') is True
        assert result.get('error_message') is not None
        assert result.get('quantity_set') == 0
        assert result.get('product_index') >= 0
        assert result.get('test_case_title') is not None
        assert result.get('test_failure_reason') is None
        assert isinstance(result.get('error_message'), str)
