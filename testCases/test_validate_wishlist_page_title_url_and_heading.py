import pytest
from flows.wishListFlow import WishListFlow


@pytest.mark.ui
@pytest.mark.regression
class TestValidateWishlistPageTitleUrlAndHeading:
    """Test: Validate WishList page title, URL, and heading."""
    
    def test_validate_wishlist_page_title_url_and_heading(self, driver, wishlist_page):
        """
        Validate Page Title, Page URL and Page Heading of WishList Page.
        
        Tests that the wishlist page loads with correct page title containing 'wishlist',
        correct URL containing 'wishlist', and a valid page heading.
        
        Verification Points:
        - Page title is valid and contains 'wishlist' keyword
        - Page URL is valid and contains 'wishlist' keyword
        - Page heading is present and not empty
        - Page loaded successfully
        
        Args:
            driver: Selenium WebDriver fixture
            wishlist_page: Fixture providing wishlist page context
        """
        # Arrange
        wishlist_flow = WishListFlow(driver)
        
        # Act
        result = wishlist_flow.validate_wishlist_page_title_url_and_heading()
        
        # Assert
        assert result is not None
        assert result.get('test_passed') is True
        assert result.get('page_loaded') is True
        assert result.get('page_title_valid') is True
        assert result.get('page_url_valid') is True
        assert result.get('page_heading_valid') is True
        assert result.get('page_title') is not None
        assert result.get('page_url') is not None
        assert result.get('page_heading') is not None
        assert result.get('test_case_title') is not None
        assert result.get('test_failure_reason') is None
