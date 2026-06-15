from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        self.find_element(locator).click()

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )
    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Дождаться открытия новой вкладки")
    def wait_for_new_tab(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.number_of_windows_to_be(2)
        )

    @allure.step("Переключиться на новую вкладку")
    def switch_to_new_tab(self):
        self.driver.switch_to.window(
            self.driver.window_handles[1]
        )

    @allure.step("Дождаться загрузки страницы")
    def wait_page_loaded(self):
        WebDriverWait(self.driver, 10).until(
            lambda d: d.current_url != "about:blank"
        )