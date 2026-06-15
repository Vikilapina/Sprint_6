from constants import BASE_URL
from pages.main_page import MainPage


class TestLogo:

    def test_scooter_logo_opens_main_page(self, driver):
        main_page = MainPage(driver)

        main_page.accept_cookies()

        main_page.click_top_order_button()
        main_page.click_scooter_logo()

        assert main_page.get_current_url() == BASE_URL

    def test_yandex_logo_opens_dzen(self, driver):
        main_page = MainPage(driver)

        main_page.accept_cookies()

        main_page.click_yandex_logo()

        main_page.wait_for_new_tab()
        main_page.switch_to_new_tab()
        main_page.wait_page_loaded()

        assert "ya.ru" in main_page.get_current_url().lower()