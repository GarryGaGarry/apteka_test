import allure
from selene import Browser
from selene.core import query
from selene.core.entity import Collection, Element
from selene.support.conditions import be

from pages.steps.base_steps import BaseSteps
from pages.locators.search_page import SearchPage
from pages.steps.item_page_steps import ItemPageSteps


class SearchPageSteps(BaseSteps):

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.locators = SearchPage

    @allure.step
    def get_search_result(self, result_must_be: bool = True) -> Collection:
        result = self.browser.all(self.locators.SEARCH_RESULTS)
        if result_must_be:
            assert len(result) > 0, 'Search results are missing'
        return result

    @allure.step
    def get_search_result_with_recipe(self, result_must_be: bool = True) -> Collection:
        search_result = self.get_search_result(result_must_be)
        search_result_after_filter = search_result.filtered_by_their(self.locators.RECIPE_FLAG, be.existing)
        if result_must_be:
            assert len(search_result_after_filter) > 0, 'Search results after recipe filter are missing'
        return search_result_after_filter

    @allure.step
    def get_item_with_recipe(self, index: int = 0) -> Element:
        search_result = self.get_search_result_with_recipe()
        return search_result[index]

    @allure.step
    def get_item_name(self, item: Element) -> str:
        return item.element(self.locators.ITEM_TITLE).get(query.text)

    @allure.step
    def go_to_item_page(self, item: Element) -> ItemPageSteps:
        item.click()
        return ItemPageSteps(self.browser)


