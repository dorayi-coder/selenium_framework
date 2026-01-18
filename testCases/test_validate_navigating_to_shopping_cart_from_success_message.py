import pytest
from flows.shoppingCartFlow import ShoppingCartFlow


@pytest.mark.ui
@pytest.mark.regression
class TestValidateNavigatingToShoppingCartFromSuccessMessage:
    """Test: Validate navigating to shopping cart page from the success message."""
    
    def test_validate_navigating_to_shopping_cart_from_success_message(self, driver, shopping_cart_with_items):
        """
        Validate navigating to shopping cart page from the success message.
        
        This test verifies:
        1. Shopping cart page loads successfully
        2. Success message is displayed on the page
        3. Success message text is captured
        4. Page title contains "cart" keyword
        5. Shopping cart is accessible from the success message
        6. Navigation and message validation both pass
        
        Args:
            driver: Selenium WebDriver fixture
            shopping_cart_with_items: Fixture providing shopping cart context with items
        """
        # Arrange
        cart_flow = ShoppingCartFlow(driver)
        
        # Act
        result = cart_flow.validate_navigating_to_shopping_cart_from_success_message()
        
        # Assert
        assert result is not None
        assert result.get('test_passed') is True
        assert result.get('page_loaded') is True
        assert result.get('success_message_displayed') is True
        assert result.get('success_message_text') is not None
        assert isinstance(result.get('success_message_text'), str)
        assert len(result.get('success_message_text', '')) > 0
        assert result.get('cart_title_verified') is True
        assert result.get('page_title') is not None
        assert 'cart' in result.get('page_title', '').lower()
        assert result.get('test_case_title') is not None
        assert result.get('test_failure_reason') is None
