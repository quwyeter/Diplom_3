import allure
from locators import Locators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step('клик на кнопку «Личный кабинет»')
    def click_account_button(self):
        self.click_to_element(Locators.ACCOUNT_BUTTON)

    @allure.step('Клик на кнопку «История заказов»')
    def click_history_button(self):
        self.click_to_element(Locators.HISTORY)

    @allure.step('Клик на кнопку «Выход»')
    def click_exit_button(self):
        self.click_to_element(Locators.EXIT)
