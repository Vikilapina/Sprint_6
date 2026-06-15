from selenium.webdriver.common.by import By


class OrderPageLocators:

    # Первая страница заказа
    FIRST_NAME = (
        By.XPATH,
        "//input[@placeholder='* Имя']"
    )

    LAST_NAME = (
        By.XPATH,
        "//input[@placeholder='* Фамилия']"
    )

    ADDRESS = (
        By.XPATH,
        "//input[@placeholder='* Адрес: куда привезти заказ']"
    )

    METRO_STATION = (
        By.XPATH,
        "//input[@placeholder='* Станция метро']"
    )

    PHONE = (
        By.XPATH,
        "//input[@placeholder='* Телефон: на него позвонит курьер']"
    )

    NEXT_BUTTON = (
        By.XPATH,
        "//button[text()='Далее']"
    )

    # Вторая страница заказа
    DELIVERY_DATE = (
        By.XPATH,
        "//input[@placeholder='* Когда привезти самокат']"
    )

    RENT_PERIOD = (
        By.CLASS_NAME,
        "Dropdown-placeholder"
    )

    BLACK_SCOOTER = (
        By.ID,
        "black"
    )

    GREY_SCOOTER = (
        By.ID,
        "grey"
    )

    COMMENT = (
        By.XPATH,
        "//input[@placeholder='Комментарий для курьера']"
    )

    ORDER_BUTTON = (
        By.XPATH,
        "(//button[text()='Заказать'])[2]"
    )

    CONFIRM_ORDER_BUTTON = (
        By.XPATH,
        "//button[text()='Да']"
    )

    SUCCESS_ORDER_HEADER = (
        By.XPATH,
        "//div[contains(text(), 'Заказ оформлен')]"
    )