import allure
import pytest
from pages.order_page import OrderPage
from data import Registration
from data import PhoneNumber
from data import Date
from data import TextData, RentalData


@pytest.mark.usefixtures("driver")
class TestOrderButton:
    @allure.title('Оформление заказа по кнопке "Заказать" в шапке страницы')
    def test_order_button_on_header_passed(self, driver):
        order = OrderPage(driver)
        order.open_page_and_cookie()
        order.click_order_button_in_header()
        order.filling_form(Registration.fake_person_info(), PhoneNumber.get_phone_number())
        order.wait_for_rent_form()
        order.input_rental_information(Date.get_date_today(), RentalData.RENTAL_DATA_1)
        order.wait_for_confirm()
        order.click_confirmation_order()
        order_title = order.get_new_order_title()
        order.wait_for_order_completed()
        assert TextData.SUCCESSFUL_ORDER_TEXT in order_title

    @allure.title('Оформление заказа по кнопке "Заказать" внизу страницы')
    def test_order_page_correct_user_data_passed(self, driver):
        order = OrderPage(driver)
        order.open_page_and_cookie()
        order.scroll_to_order_button()
        order.click_order_button_in_bottom()
        order.filling_form(Registration.fake_person_info(), PhoneNumber.get_phone_number())
        order.wait_for_rent_form()
        order.input_rental_information(Date.get_date_tomorrow(), RentalData.RENTAL_DATA_2)
        order.wait_for_confirm()
        order.click_confirmation_order()
        order_title = order.get_new_order_title()
        order.wait_for_order_completed()
        assert TextData.SUCCESSFUL_ORDER_TEXT in order_title