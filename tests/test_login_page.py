import allure
from data import Data
from locators import Locators
from pages.login_page import LoginPage


class TestLoginPage:
    @allure.title('Тест переход по клику на «Личный кабинет»')
    def test_click_account_button(self, driver):
        page = LoginPage(driver)
        page.click_account_button()
        assert page.get_current_url == Data.LOGIN_URL or Data.PROFILE_URL

    @allure.title('Тест переход в раздел «История заказов»')
    def test_go_to_history(self, driver):
        page = LoginPage(driver)
        page.login()
        page.click_account_button()
        page.click_history_button()
        assert page.find_element_by_locator_with_wait(Locators.ORDER)

    @allure.title('Тест выход из аккаунта')
    def test_exit(self, driver):
        page = LoginPage(driver)
        page.login()
        page.click_account_button()
        page.click_exit_button()
        assert page.find_element_by_locator_with_wait(Locators.ENTER_BUTTON)
