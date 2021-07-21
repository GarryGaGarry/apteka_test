import time
from selene import Browser
import allure

from configuration import Configuration
from pages.locators.base_page import BasePage


class BaseSteps:

    def __init__(self, browser: Browser):
        self.browser = browser
        self.base_locators = BasePage

    @allure.step
    def close_notification(self):
        self.browser.element(self.base_locators.CONFIRM_CITY_BUTTON).click()
        if Configuration.browser_type == 'mobile':
            self.browser.element(self.base_locators.NOTIFICATION_CLOSE_BUTTON).click()
        return self

    @allure.step
    def search(self, search_query: str) -> 'SearchPageSteps':
        self.close_notification()
        self.browser.element(self.base_locators.SEARCH_INPUT).type(search_query).press_enter()
        from pages.steps.search_page_steps import SearchPageSteps
        return SearchPageSteps(self.browser)

