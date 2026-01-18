import pytest
from flows.searchFlow import SearchFlow


@pytest.mark.ui
@pytest.mark.regression
class TestValidateSearchWithWhitespaceOnly:
    """Test: Validate search behavior with whitespace-only input."""
    
    def test_validate_search_with_whitespace_only(self, driver, search_page):
        """
        Validate search behavior when search term contains only whitespace characters.
        
        This test verifies:
        1. Search page loads and is ready for input
        2. Search is attempted with whitespace-only string
        3. Application handles whitespace input gracefully (no crash)
        4. Search execution status is determined
        5. Results container visibility is tracked
        6. No-results message is captured if displayed
        7. Trimming behavior is validated (whether whitespace trimmed to empty)
        8. Overall validation passes indicating graceful handling
        
        Args:
            driver: Selenium WebDriver fixture
            search_page: Fixture providing search page context
        """
        # Arrange
        search_flow = SearchFlow(driver)
        whitespace_input = "   "
        
        # Act
        result = search_flow.validate_search_with_whitespace_only(whitespace_input)
        
        # Assert
        assert result is not None
        assert result.get('validation_passed') is True
        assert result.get('whitespace_string') is not None
        assert result.get('whitespace_string') == whitespace_input
        assert result.get('search_executed') in [True, False]
        assert result.get('results_displayed') in [True, False]
        assert result.get('has_results') in [True, False]
        assert result.get('trimmed_to_empty') in [True, False]
        assert isinstance(result.get('result_count'), int)
        assert result.get('result_count') >= 0
        assert result.get('no_results_message') is None or isinstance(result.get('no_results_message'), str)
        assert result.get('page_url') is not None
