import allure
import pytest
from pages.steps.main_page_steps import MainPageSteps


@pytest.mark.search
@pytest.mark.parametrize('search_query', ['фенибут'])
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature('Search')
@allure.story('In search results products with the same name as in the product card')
def test_search_result_name_equals_item_page_title(browser, search_query):
    # Given
    main_page = MainPageSteps(browser).open()

    # When
    search_page = main_page.search(search_query)
    item_with_recipe = search_page.get_item_with_recipe()
    item_name_from_search_page = search_page.get_item_name(item_with_recipe)
    item_page = search_page.go_to_item_page(item_with_recipe)
    title_item_text = item_page.get_title()

    # Then
    error_message = f"Item name({item_name_from_search_page}) from the search results does not equal" \
                    f" title({title_item_text}) from the item page"
    with allure.step("Check in search results products with the same name as in the product card"):
        assert title_item_text == item_name_from_search_page, error_message
