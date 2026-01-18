import pytest
from flows.searchFlow import SearchFlow


@pytest.mark.ui
@pytest.mark.regression
class TestValidateSearchWithRepeatedCharacters:
    """Test: Validate search behavior with repeated character input."""
    
    def test_validate_search_with_repeated_characters(self, driver, search_page):
        """
        Validate search behavior when search term contains only repeated characters.
        
        This test verifies:
        1. Search page loads and is ready for input
        2. Search is attempted with repeated character string (default 'aaaaaaa')
        3. Application handles repeated character input gracefully (no crash)
        4. Search execution status is determined
        5. Results container visibility is tracked
        6. Product results or no-results message is captured
        7. First product name is retrieved if results exist
        8. Search handled gracefully without errors
        9. Overall validation passes
        
        Args:
            driver: Selenium WebDriver fixture
            search_page: Fixture providing search page context
        """
        # Arrange
        search_flow = SearchFlow(driver)
        character = 'a'
        repetition_count = 7
        
        # Act
        result = search_flow.validate_search_with_repeated_characters(character, repetition_count)
        
        # Assert
        assert result is not None
        assert result.get('validation_passed') is True
        assert result.get('repeated_string') is not None
        assert result.get('repeated_string') == (character * repetition_count)
        assert result.get('search_executed') in [True, False]
        assert result.get('results_displayed') in [True, False]
        assert result.get('has_results') in [True, False]
        assert result.get('search_handled_gracefully') is True
        assert isinstance(result.get('result_count'), int)
        assert result.get('result_count') >= 0
        assert result.get('first_product_name') is None or isinstance(result.get('first_product_name'), str)
        assert result.get('no_results_message') is None or isinstance(result.get('no_results_message'), str)
        assert result.get('page_url') is not None
