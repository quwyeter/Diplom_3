from selenium.webdriver.common.by import By


class Locators:
    BURGER_TEXT = (By.XPATH, '//h1[text()="Соберите бургер"]')
    FORGOT_PASSWORD_BUTTON = (By.XPATH, '//a[text()="Восстановить пароль"]')
    RECOVER_BUTTON = (By.XPATH, '//button[text() = "Восстановить"]')
    SAVE_BUTTON = (By.XPATH, '//button[text()="Сохранить"]')

    SHOW_PASSWORD_BUTTON = (By.XPATH, '//*[@class="input__icon input__icon-action"]')
    HIDE_PASSWORD_BUTTON = SHOW_EYE_PASSWORD = (
        By.XPATH, '//div[@class="input pr-6 pl-6 input_type_text input_size_default input_status_active"]')

    EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/following::input')
    PASSWORD_INPUT = (By.XPATH, '//input[@name = "Пароль"]')
    ENTER_BUTTON = (By.XPATH, '//Button[text()="Войти"]')

    ACCOUNT_BUTTON = (By.XPATH, '//a[@href="/account"]')
    HISTORY = (By.XPATH, '//a[text()="История заказов"]')
    EXIT = (By.XPATH, '//button[text()="Выход"]')
    ORDER = (By.XPATH, '//h2[text()="Spicy краторный бургер"]')

    CONSTRUCTOR = (By.XPATH, '//p[text()="Конструктор"]')
    CONSTRUCTOR_TEXT = (By.XPATH, '//h1[text()="Соберите бургер"]')
    ORDER_LIST = (By.XPATH, '//p[text()="Лента Заказов"]')
    ORDER_LIST_TEXT = (By.XPATH, '//h1[text()="Лента заказов"]')
    INGREDIENT = (By.XPATH, '//img[@alt="Флюоресцентная булка R2-D3"]')
    DETAILS = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    CROSS_BUTTON = (By.XPATH, '//button[@type="button"]')
    DRAG_BUN = (By.XPATH, '//span[text()="Перетяните булочку сюда (верх)"]')
    INGREDIENT_COUNT = (By.CLASS_NAME, 'counter_counter__num__3nue1')
    MAKE_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')
    ORDER_ID_TEXT = (By.XPATH, '//p[text()="идентификатор заказа"]')
    ORDER_ID = (By.XPATH, '//h2[contains(@class, "modal__title")]')
    ORDER_ID_9999 = (By.XPATH, '//h2[text()="9999"]')


    ALL_TIME_ORDER_COUNT = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')
    TODAY_ORDER_COUNT = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')
    ORDER_HISTORY = (By.XPATH, '//div[contains(@class,"OrderHistory_textBox")]/p')
    ORDER_ID_FIRST = (By.XPATH, '(//div[contains(@class,"OrderHistory_textBox")]/p)')
    ORDER_ID_LAST = (By.XPATH, '(//p[@class = "text text_type_digits-default"])[last()]')
    ORDER_HISTORY_BUTTON = (By.XPATH, '//div[contains(@class,"OrderHistory_dataBox")]')
    ORDER_PROGRESS = (By.XPATH, '//ul[contains(@class,"orderListReady")]/li')
    ORDER_DETAILS = (By.XPATH, '//div[contains(@class,"Modal_orderBox")]')

