import allure
import pytest
from selenium import webdriver
from data import Data
from locators import Locators
from pages.main_page import MainPage


class TestMainPage:
    @allure.title('Тест перехода по клику на «Лента заказов»')
    def test_click_order_list_button(self, driver):
        page = MainPage(driver)
        page.click_order_list_button()
        assert page.find_element_by_locator_with_wait(Locators.ORDER_LIST_TEXT)

    @allure.title('Тест перехода по клику на «Конструктор»')
    def test_click_constructor_button(self, driver):
        page = MainPage(driver)
        page.click_order_list_button()
        page.click_constructor_button()
        assert page.find_element_by_locator_with_wait(Locators.CONSTRUCTOR_TEXT)

    @allure.title('Тест если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_to_ingredient_pop_up_window_with_details(self, driver):
        page = MainPage(driver)
        page.click_to_ingredient()
        assert page.find_element_by_locator_with_wait(Locators.DETAILS)

    @allure.title('Тест всплывающее окно закрывается кликом по крестику')
    def test_click_cross_button(self, driver):
        page = MainPage(driver)
        page.click_to_ingredient()
        page.click_cross_button()
        assert page.check_window_closed

    @allure.title('Тест залогиненный пользователь может оформить заказ')
    def test_make_order(self, driver):
        page = MainPage(driver)
        page.make_order()
        assert page.find_element_by_locator_with_wait(Locators.ORDER_ID)

    @allure.title('Тест если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order(self, driver):
        page = MainPage(driver)
        page.click_order_list_button()
        page.click_order_button()
        assert page.find_element_by_locator_with_wait(Locators.ORDER_HISTORY)

    @allure.title('Тест заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_user_orders_from_history_displayed_on_the_order_feed_page(self, driver):
        page = MainPage(driver)
        order_history_id = page.get_order_history_id()
        order_list_id = page.get_order_list_id()
        assert order_history_id == order_list_id

    @allure.title('Тест при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_when_creating_a_new_order_counter_increases_for_all_time(self, driver):
        page = MainPage(driver)
        counter_1 = page.get_counter_all_time()
        page.make_order()
        page.click_cross_button()
        counter_2 = page.get_counter_all_time()
        assert counter_2 >= counter_1

    @allure.title('Тест при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_when_creating_a_new_order_counter_increases_today(self, driver):
        page = MainPage(driver)
        counter_1 = page.get_counter_today()
        page.make_order()
        page.click_cross_button()
        counter_2 = page.get_counter_today()
        assert counter_2 >= counter_1

    @allure.title('Тест после оформления заказа его номер появляется в разделе В работе')
    def test_after_order_number_appears_in_progress_section(self, driver):
        page = MainPage(driver)
        id1 = page.get_order_id()
        page.click_cross_button()
        id2 = page.get_order_id_from_progress_section()
        assert id1 == id2
