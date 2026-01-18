import pytest
from flows.wishListFlow import WishListFlow


@pytest.mark.ui
@pytest.mark.regression
class TestVerifyWishListReflectsUpdatedProductPrice:
    """Test: Verify Wish List reflects updated product price."""
    
    def test_verify_wish_list_reflects_updated_product_price(self, driver, wishlist_page):
        """
        Verify Wish List reflects updated product price.
        
        Tests that product prices are correctly displayed in the wishlist and
        reflect any updated pricing information.
        
        Verification Points:
        - Wishlist page loads successfully
        - Product is found in wishlist
        - Product price is valid and not zero
        - All product prices are displayed in wishlist
        - Price display mechanism is working
        
        Args:
            driver: Selenium WebDriver fixture
            wishlist_page: Fixture providing wishlist page context
        """
        # Arrange
        wishlist_flow = WishListFlow(driver)
        product_name = "Test Product"
        
        # Act
        result = wishlist_flow.verify_wish_list_reflects_updated_product_price(product_name)
        
        # Assert
        assert result is not None
        assert result.get('test_passed') is True
        assert result.get('product_found_in_wishlist') is True
        assert result.get('price_valid') is True
        assert result.get('prices_display_working') is True
        assert result.get('product_price') is not None
        assert result.get('product_price') > 0
        assert result.get('total_products_with_prices') > 0
        assert result.get('all_prices_displayed') is not None
        assert isinstance(result.get('all_prices_displayed'), list)
        assert result.get('product_name') == product_name
        assert result.get('test_case_title') is not None
        assert result.get('test_failure_reason') is None
