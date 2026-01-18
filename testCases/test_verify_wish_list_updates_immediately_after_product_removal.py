import pytest
from flows.wishListFlow import WishListFlow


@pytest.mark.ui
@pytest.mark.regression
class TestVerifyWishListUpdatesImmediatelyAfterProductRemoval:
    """Test: Verify Wish List updates immediately after product removal."""
    
    def test_verify_wish_list_updates_immediately_after_product_removal(self, driver, wishlist_page):
        """Verify Wish List updates immediately after product removal.
        
        Comprehensive test validating that wishlist updates immediately when a product is removed.
        Verifies removal execution, count decrease, and product no longer present in wishlist.
        
        Verification Points:
        - Product exists in wishlist before removal
        - Remove operation executes successfully
        - Initial wishlist count captured
        - Updated wishlist count captured and decreased
        - Product removed from wishlist list
        - Products before and after removal captured
        - Overall test passes only if all conditions met
        
        Args:
            driver: Selenium WebDriver instance from pytest fixture
            wishlist_page: Wishlist page object fixture for wishlist operations
        """
        # Arrange
        wishlist_flow = WishListFlow(driver)
        product_name = "Test Product"
        
        # Act
        result = wishlist_flow.verify_wish_list_updates_immediately_after_product_removal(product_name)
        
        # Assert
        assert result is not None
        assert result.get('test_passed') is True
        assert result.get('product_existed_before') is True
        assert result.get('remove_executed') is True
        assert result.get('wishlist_count_decreased') is True
        assert result.get('product_removed_from_list') is True
        assert result.get('initial_wishlist_count') is not None
        assert result.get('updated_wishlist_count') is not None
        assert result.get('updated_wishlist_count') < result.get('initial_wishlist_count')
        assert result.get('products_before_removal') is not None
        assert result.get('products_after_removal') is not None
        assert isinstance(result.get('products_before_removal'), list)
        assert isinstance(result.get('products_after_removal'), list)
