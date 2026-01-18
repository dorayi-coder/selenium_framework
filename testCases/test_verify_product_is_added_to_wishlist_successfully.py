import pytest
from flows.wishListFlow import WishListFlow


@pytest.mark.ui
@pytest.mark.regression
class TestVerifyProductIsAddedToWishlistSuccessfully:
    """Test: Verify product is added to wishlist successfully."""
    
    def test_verify_product_is_added_to_wishlist_successfully(self, driver, wishlist_page):
        """
        Verify product is added to wishlist successfully.
        
        Tests that a product can be added to the wishlist and the wishlist
        updates immediately with the new product.
        
        Verification Points:
        - Add to wishlist operation executes successfully
        - Wishlist item count increases after adding product
        - Product is found in wishlist after add
        - Product name is correctly stored
        - All results fields are valid
        
        Args:
            driver: Selenium WebDriver fixture
            wishlist_page: Fixture providing wishlist page context
        """
        # Arrange
        wishlist_flow = WishListFlow(driver)
        product_name = "Test Product"
        
        # Act
        result = wishlist_flow.verify_product_is_added_to_wishlist_successfully(product_name)
        
        # Assert
        assert result is not None
        assert result.get('test_passed') is True
        assert result.get('add_to_wishlist_executed') is True
        assert result.get('wishlist_count_increased') is True
        assert result.get('product_found_in_wishlist') is True
        assert result.get('product_name') == product_name
        assert result.get('initial_wishlist_count') >= 0
        assert result.get('updated_wishlist_count') > result.get('initial_wishlist_count')
        assert result.get('products_in_wishlist') is not None
        assert isinstance(result.get('products_in_wishlist'), list)
        assert result.get('test_case_title') is not None
        assert result.get('test_failure_reason') is None
