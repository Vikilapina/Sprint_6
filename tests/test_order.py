import pytest

from data.order_data import ORDER_DATA
from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.mark.parametrize(
    "first_name, last_name, address, metro, phone, date, rent_period, color, comment",
    ORDER_DATA
)
def test_open_order_form(
    driver,
    first_name,
    last_name,
    address,
    metro,
    phone,
    date,
    rent_period,
    color,
    comment
):
    main_page = MainPage(driver)

    main_page.accept_cookies()
    main_page.click_top_order_button()

    order_page = OrderPage(driver)

    order_page.fill_first_name(first_name)
    order_page.fill_last_name(last_name)
    order_page.fill_address(address)
    order_page.select_metro_station(metro)
    order_page.fill_phone(phone)

    order_page.click_next_button()

    order_page.fill_delivery_date(date)

    order_page.click_rent_period()
    order_page.select_rent_period(rent_period)

    if color == "black":
        order_page.select_black_scooter()
    else:
        order_page.select_grey_scooter()

    order_page.fill_comment(comment)

    order_page.click_order_button()
    order_page.confirm_order()

    assert "Заказ оформлен" in order_page.get_success_order_text()