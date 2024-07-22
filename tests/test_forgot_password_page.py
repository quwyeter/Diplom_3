import allure
from data import Data
from locators import Locators
from pages.forgot_password_page import ForgotPasswordPage


class TestLoginPage:
    @allure.title('Тест переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_click_forgot_password_button_go_to_forgot_password_page(self, driver):
        page = ForgotPasswordPage(driver)
        page.get_url(Data.LOGIN_URL)
        page.click_forgot_password_button()
        assert page.get_current_url() == Data.FORGOT_PASSWORD_URL

    @allure.title('Тест ввод почты и клик по кнопке «Восстановить»')
    def test_enter_mail_and_clicking_restore_button(self, driver):
        page = ForgotPasswordPage(driver)
        page.get_url(Data.FORGOT_PASSWORD_URL)
        page.enter_email()
        page.click_recover_button()
        page.find_element_by_locator_with_wait(Locators.SAVE_BUTTON)
        assert page.get_current_url() == Data.RESET_PASSWORD_URL

    @allure.title('Тест клик по кнопке показать пароль')
    def test_click_show_password_button(self, driver):
        page = ForgotPasswordPage(driver)
        page.get_url(Data.LOGIN_URL)
        page.click_show_password_button()
        assert page.find_hide_password_button()

    @allure.title('Тест клик по кнопке скрыть пароль')
    def test_click_hide_password_button(self, driver):
        page = ForgotPasswordPage(driver)
        page.get_url(Data.LOGIN_URL)
        page.click_show_password_button()
        page.click_hide_password_button()
        assert page.find_show_password_button()
