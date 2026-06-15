from selenium.webdriver.common.by import By


class MainPageLocators:

    # Кнопки заказа
    TOP_ORDER_BUTTON = (
        By.XPATH,
        "(//button[text()='Заказать'])[1]"
    )

    BOTTOM_ORDER_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'Button_Middle')]"
    )

    # Логотипы
    SCOOTER_LOGO = (
        By.CLASS_NAME,
        "Header_LogoScooter__3lsAR"
    )

    YANDEX_LOGO = (
        By.CLASS_NAME,
        "Header_LogoYandex__3TSOI"
    )

    COOKIE_BUTTON = (
        By.ID,
        "rcc-confirm-button"
    )

    # FAQ
    QUESTION_ID = "accordion__heading-{}"
    ANSWER_ID = "accordion__panel-{}"