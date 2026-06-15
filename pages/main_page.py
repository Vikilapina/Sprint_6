import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):

    @allure.step("Нажать верхнюю кнопку Заказать")
    def click_top_order_button(self):
        self.click_element(MainPageLocators.TOP_ORDER_BUTTON)

    @allure.step("Нажать нижнюю кнопку Заказать")
    def click_bottom_order_button(self):
        self.click_element(MainPageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step("Нажать логотип Самокат")
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Нажать логотип Яндекс")
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    @allure.step("Принять cookies")
    def accept_cookies(self):
        self.click_element(MainPageLocators.COOKIE_BUTTON)

    @allure.step("Нажать вопрос FAQ")
    def click_question(self, index):
        locator = (
            By.ID,
            MainPageLocators.QUESTION_ID.format(index)
        )

        element = self.find_element(locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            element
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    @allure.step("Дождаться ответа FAQ")
    def wait_for_answer(self, index):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (
                    By.ID,
                    MainPageLocators.ANSWER_ID.format(index)
                )
            )
        )
    
    @allure.step("Получить текст ответа FAQ")
    def get_answer_text(self, index):
        locator = (
            By.ID,
            MainPageLocators.ANSWER_ID.format(index)
        )
        return self.find_element(locator).text
    