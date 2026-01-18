import pytest
from flows.searchFlow import SearchFlow


@pytest.mark.ui
@pytest.mark.regression
class TestValidateSearchUsingSearchCriteriaField:
    """Test: Validate search using search criteria field."""
    
    def test_validate_search_using_search_criteria_field(self, driver, search_page):
        """
        Validate the search criteria field functionality end-to-end.
        
        This test validates that:
        - Search input field is visible and accessible
        - Input field properly accepts search criteria
        - Search button is visible and functional
        - Search can be successfully submitted
        - Search results are displayed after submission
        - Input field value matches entered criteria
        - Overall validation passes
        
        Args:
            driver: Selenium WebDriver instance from pytest fixture
            search_page: Search page context fixture
        
        Assert:
            - result dictionary is not None
            - validation_passed is True
            - input_field_visible is True
            - input_field_accepts_input is True
            - search_button_visible is True
            - search_submitted is True
            - results_displayed is True
            - search_criteria is not None
        """
        # Arrange
        search_flow = SearchFlow(driver)
        search_criteria = "laptop"
        
        # Act
        result = search_flow.validate_search_using_search_criteria_field(search_criteria)
        
        # Assert
        assert result is not None
        assert result.get('validation_passed') is True
        assert result.get('input_field_visible') is True
        assert result.get('input_field_accepts_input') is True
        assert result.get('search_button_visible') is True
        assert result.get('search_submitted') is True
        assert result.get('results_displayed') is True
        assert result.get('search_criteria') is not None
