import pytest
from flows.productCompareFlow import ProductCompareFlow


@pytest.mark.ui
@pytest.mark.regression
class TestVerifySameProductIsNotDuplicatedInCompareList:
    """
    Test suite for verifying duplicate prevention in product comparison list.
    
    Tests that the same product cannot be added multiple times to the comparison list,
    preventing duplicate entries.
    """

    def test_verify_same_product_is_not_duplicated_in_compare_list(self, driver, search_results_page_with_products):
        """
        Test: Verify same product is not duplicated in Compare list.
        
        Verifies that:
        - Product can be added to comparison list
        - Adding the same product again does not create a duplicate
        - Product count remains the same after duplicate add attempt
        - Comparison list prevents duplicate entries
        
        Args:
            driver: Selenium WebDriver fixture
            search_results_page_with_products: Fixture providing search results page with available products
        
        Asserts:
            - Test result is not None
            - Test passes successfully
            - Product count after first add is available
            - Product count after second add is available
            - Both counts are equal (no duplication occurred)
            - Test failure reason is None when no duplication detected
        """
        # Arrange
        product_compare_flow = ProductCompareFlow(driver)
        
        # Act
        result = product_compare_flow.verify_same_product_is_not_duplicated_in_compare_list()
        
        # Assert
        assert result is not None, "Duplicate prevention validation result should not be None"
        assert result.get('test_passed') is True, \
            f"Duplicate prevention validation failed: {result.get('test_failure_reason')}"
        assert result.get('count_after_first_add') is not None, \
            "Product count after first add should be available"
        assert result.get('count_after_second_add') is not None, \
            "Product count after second add should be available"
        assert result.get('count_after_first_add') == result.get('count_after_second_add'), \
            "Product count should remain the same when adding the same product again (no duplication)"
        assert result.get('test_failure_reason') is None, \
            "Test failure reason should be None when duplicate is prevented"
