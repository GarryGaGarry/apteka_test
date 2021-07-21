from __future__ import annotations

import allure
from selene import Browser

from configuration import Configuration
from pages.steps.base_steps import BaseSteps
from pages.locators.main_page import MainPage


class MainPageSteps(BaseSteps):
    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.url = Configuration.base_url
        self.locators = MainPage

    @allure.step
    def open(self) -> MainPageSteps:
        self.browser.open(self.url)
        return self
