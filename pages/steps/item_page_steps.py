import allure
from selene import Browser
from selene.core import query

from pages.steps.base_steps import BaseSteps
from pages.locators.item_page import ItemPage


class ItemPageSteps(BaseSteps):

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.locators = ItemPage

    @allure.step
    def get_title(self) -> str:
        return self.browser.element(self.locators.TITLE).get(query.text)
