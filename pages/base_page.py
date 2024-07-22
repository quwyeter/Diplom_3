import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from data import Data
from locators import Locators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_url(self, geturl):
        self.driver.get(geturl)

    @allure.step('Поиск элемента по локатору с ожиданием')
    def find_element_by_locator_with_wait(self, locator):
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Клик по элементу')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Добавить текст в элемент')
    def add_text_to_element(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Получить текст элемента')
    def get_text_from_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Видимость элемента')
    def invisibility_element(self, locator):
        WebDriverWait(self.driver, 20).until(ec.invisibility_of_element_located(locator))

    @allure.step('Ждать url')
    def wait_url(self, url):
        WebDriverWait(self.driver, 20).until(ec.url_to_be(url))

    @allure.step('Переключить окно')
    def switch_window(self):
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.find_element_by_locator_with_wait(locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Получить текущий url')
    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    @allure.step('Перетаскивание элемента')
    def dnd_element(self, locator1, locator2):
        source = self.find_element_by_locator_with_wait(locator1)
        target = self.find_element_by_locator_with_wait(locator2)
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target)
        action.perform()

    def login(self):
        self.get_url(Data.LOGIN_URL)
        self.add_text_to_element(Locators.EMAIL_INPUT, Data.TEST_EMAIL)
        self.add_text_to_element(Locators.PASSWORD_INPUT, Data.TEST_PASSWORD)
        self.click_to_element(Locators.ENTER_BUTTON)
