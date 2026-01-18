import pytest
from flows.wishListFlow import WishListFlow


@pytest.mark.ui
@pytest.mark.regression
class TestValidateAddingProductToWishlistFromSearchResultPage:
    """Test: Validate adding product to WishList from search result page."""
    
    def test_validate_adding_product_to_wishlist_from_search_result_page(self, driver, search_results_page_with_products):
        """
        Validate adding a product to WishList page from the search Result page.
        
        Tests the complete workflow of searching for a product, adding it to wishlist
        from search results, and verifying it appears in the wishlist.
        
        Verification Points:
        - Product search is executed successfully
        - Product is found in search results
        - Add to wishlist button works from search results
        - Wishlist page loads after add
        - Product appears in wishlist
        - Wishlist item count increases
        
        Args:
            driver: Selenium WebDriver fixture
            search_results_page_with_products: Fixture providing search results with products
        """
        # Arrange
        wishlist_flow = WishListFlow(driver)
        product_name = "Test Product"
        
        # Act
        result = wishlist_flow.validate_adding_product_to_wishlist_from_search_result_page(product_name)
        
        # Assert
        assert result is not None
        assert result.get('test_passed') is True
        assert result.get('search_executed') is True
        assert result.get('product_found_in_search_results') is True
        assert result.get('add_to_wishlist_from_search_executed') is True
        assert result.get('wishlist_page_loaded') is True
        assert result.get('product_found_in_wishlist') is True
        assert result.get('product_name') == product_name
        assert result.get('wishlist_item_count') > 0
        assert result.get('products_in_wishlist') is not None
        assert isinstance(result.get('products_in_wishlist'), list)
        assert result.get('test_case_title') is not None
        assert result.get('test_failure_reason') is None
