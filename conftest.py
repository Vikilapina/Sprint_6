import pytest
from selenium import webdriver
from constants import BASE_URL


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(BASE_URL)

    yield driver
    driver.quit()