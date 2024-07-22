import allure
from locators import Locators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Клик по кнопке Конструктор')
    def click_constructor_button(self):
        self.click_to_element(Locators.CONSTRUCTOR)

    @allure.step('Клик по кнопке Лента заказов')
    def click_order_list_button(self):
        self.click_to_element(Locators.ORDER_LIST)

    @allure.step('Клик по ингредиенту')
    def click_to_ingredient(self):
        self.click_to_element(Locators.INGREDIENT)

    @allure.step('Клик на крестик')
    def click_cross_button(self):
        self.click_to_element(Locators.CROSS_BUTTON)

    @allure.step('Проверка закрытия всплывающего окна')
    def check_window_closed(self):
        return self.invisibility_element(Locators.DETAILS)


    @allure.step('Добавление ингредиента в заказ')
    def add_ingredient_to_order(self):
        self.dnd_element(Locators.INGREDIENT, Locators.DRAG_BUN)

    @allure.step('Получение количества ингредиентов')
    def get_ingredient_count(self):
        self.get_text_from_element(Locators.INGREDIENT_COUNT)

    @allure.step('Создание заказа')
    def make_order(self):
        self.login()
        self.add_ingredient_to_order()
        self.click_to_element(Locators.MAKE_ORDER_BUTTON)

    @allure.step('Клик по кнопке «История заказов»')
    def click_order_history_button(self):
        self.click_to_element(Locators.ORDER_HISTORY)

    @allure.step('Клик на заказ')
    def click_order_button(self):
        self.click_to_element(Locators.ORDER_HISTORY_BUTTON)

    @allure.step('Получить айди последнего заказа из истории заказов')
    def get_order_history_id(self):
        self.make_order()
        self.click_cross_button()
        self.click_to_element(Locators.ACCOUNT_BUTTON)
        self.click_to_element(Locators.HISTORY)
        self.scroll_to_element(Locators.ORDER_ID_LAST)
        return self.get_text_from_element(Locators.ORDER_ID_LAST)

    @allure.step('Получить айди заказа из ленты заказов')
    def get_order_list_id(self):
        self.click_order_list_button()
        self.click_order_button()
        return self.get_text_from_element(Locators.ORDER_ID_FIRST)

    @allure.step('Получить количество заказов за всё время')
    def get_counter_all_time(self):
        self.click_order_list_button()
        self.scroll_to_element(Locators.ALL_TIME_ORDER_COUNT)
        return self.get_text_from_element(Locators.ALL_TIME_ORDER_COUNT)

    @allure.step('Получить количество заказов за сегодня')
    def get_counter_today(self):
        self.click_order_list_button()
        self.scroll_to_element(Locators.TODAY_ORDER_COUNT)
        return self.get_text_from_element(Locators.TODAY_ORDER_COUNT)

    @allure.step('Получить айди созданного заказа')
    def get_order_id(self):
        self.make_order()
        self.invisibility_element(Locators.ORDER_ID_9999)
        self.scroll_to_element(Locators.ORDER_ID)
        return self.get_text_from_element(Locators.ORDER_ID)

    @allure.step('Получить айди из раздела в работе')
    def get_order_id_from_progress_section(self):
        self.click_order_list_button()
        self.scroll_to_element(Locators.ORDER_PROGRESS)
        return self.get_text_from_element(Locators.ORDER_PROGRESS)
