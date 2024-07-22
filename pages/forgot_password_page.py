import allure
from helpers import Helpers
from locators import Locators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    @allure.step('Клик на кнопку «Восстановить пароль»')
    def click_forgot_password_button(self):
        self.click_to_element(Locators.FORGOT_PASSWORD_BUTTON)

    @allure.step('Ввод почты')
    def enter_email(self):
        self.add_text_to_element(Locators.EMAIL_INPUT, Helpers.EMAIL)

    @allure.step('Клик по кнопке «Восстановить»')
    def click_recover_button(self):
        self.click_to_element(Locators.RECOVER_BUTTON)

    @allure.step('найти кнопку показать пароль')
    def find_show_password_button(self):
        return self.find_element_by_locator_with_wait(Locators.SHOW_PASSWORD_BUTTON)

    @allure.step('найти кнопку скрыть пароль')
    def find_hide_password_button(self):
        return self.find_element_by_locator_with_wait(Locators.HIDE_PASSWORD_BUTTON)

    @allure.step('клик по кнопке показать пароль')
    def click_show_password_button(self):
        self.click_to_element(Locators.SHOW_PASSWORD_BUTTON)

    @allure.step('клик по кнопке скрыть пароль')
    def click_hide_password_button(self):
        self.click_to_element(Locators.HIDE_PASSWORD_BUTTON)
