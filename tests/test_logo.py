from constants import BASE_URL
from pages.main_page import MainPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def test_scooter_logo_opens_main_page(driver):
    main_page = MainPage(driver)

    main_page.accept_cookies()

    main_page.click_top_order_button()
    main_page.click_scooter_logo()

    assert driver.current_url == BASE_URL


def test_yandex_logo_opens_dzen(driver):
    main_page = MainPage(driver)

    main_page.accept_cookies()

    main_page.click_yandex_logo()

    WebDriverWait(driver, 10).until(
        expected_conditions.number_of_windows_to_be(2)
    )

    driver.switch_to.window(driver.window_handles[1])

    WebDriverWait(driver, 10).until(
        lambda d: d.current_url != "about:blank"
    )

    assert "ya.ru" in driver.current_url.lower()