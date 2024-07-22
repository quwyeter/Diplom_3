import pytest
from selenium import webdriver
from data import Data


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(Data.MAIN_URL)
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(Data.MAIN_URL)
    yield driver
    driver.quit()
