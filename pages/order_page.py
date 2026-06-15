from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    def fill_first_name(self, first_name):
        self.send_keys(
            OrderPageLocators.FIRST_NAME,
            first_name
        )

    def fill_last_name(self, last_name):
        self.send_keys(
            OrderPageLocators.LAST_NAME,
            last_name
        )

    def fill_address(self, address):
        self.send_keys(
            OrderPageLocators.ADDRESS,
            address
        )

    def fill_phone(self, phone):
        self.send_keys(
            OrderPageLocators.PHONE,
            phone
        )

    def click_next_button(self):
        self.click_element(
            OrderPageLocators.NEXT_BUTTON
        )

    def select_metro_station(self, station):
        self.send_keys(
            OrderPageLocators.METRO_STATION,
            station
        )

        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//div[contains(text(), '{station}')]"
                )
            )
        ).click()

    def fill_delivery_date(self, date):
        element = self.find_element(
            OrderPageLocators.DELIVERY_DATE
        )

        element.send_keys(date)
        element.send_keys(Keys.ENTER)

    def click_rent_period(self):
        self.click_element(
            OrderPageLocators.RENT_PERIOD
        )

    def select_rent_period(self, period):
        self.driver.find_element(
            By.XPATH,
            f"//div[text()='{period}']"
        ).click()

    def select_black_scooter(self):
        self.click_element(
            OrderPageLocators.BLACK_SCOOTER
        )

    def select_grey_scooter(self):
        self.click_element(
            OrderPageLocators.GREY_SCOOTER
        )

    def fill_comment(self, comment):
        self.send_keys(
            OrderPageLocators.COMMENT,
            comment
        )

    def click_order_button(self):
        self.click_element(
            OrderPageLocators.ORDER_BUTTON
        )

    def confirm_order(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(
                OrderPageLocators.CONFIRM_ORDER_BUTTON
            )
        ).click()

    def get_success_order_text(self):
        return self.find_element(
            OrderPageLocators.SUCCESS_ORDER_HEADER
        ).text