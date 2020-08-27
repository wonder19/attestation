import time

import allure
import pytest
from pytest_testrail.plugin import pytestrail

from common.constants import DepositPageConstants
from model.deposit import DepositData


class TestDeposit:

    @allure.suite("DepositSuite")
    @allure.description("Open Deposit test")
    @allure.tag("Testrail C1")
    @pytestrail.case("C1")
    def test_open_deposit(self, login):
        """
        Steps.
        1) Authorize
        2) Deposit tab
        3) Choose  currency
        4) Choose term
        5) Chose rate
        6) Input deposit amount
        7) Click continue button
        8) Accept conditions
        9) Click continue button
        """
        deposit_data = DepositData().random()
        login.open_main_page()

        login.main_page.deposit_button_click()
        login.deposit_page.new_deposit_button_click()
        login.deposit_page.fill_deposit_condition(deposit_data)
        login.deposit_page.amount_input_send_keys(50000)
        login.deposit_page.submit_button_click()

    @allure.suite("DepositSuite")
    @allure.description("Open Deposit test with incorrect date condition")
    @allure.tag("Testrail C9")
    @pytestrail.case("C9")
    def test_open_deposit_with_incorrect_date(self, login):
        """
        Steps.
        1) Authorize
        2) Deposit tab
        3) Fill deposit condition
        4) Fill incorrect deposit date end value
        """
        value = '111'
        deposit_data = DepositData().random()
        login.open_main_page()

        login.main_page.deposit_button_click()
        login.deposit_page.new_deposit_button_click()
        login.deposit_page.fill_deposit_condition(deposit_data)
        time.sleep(5)
        login.deposit_page.end_deposit_date_input_send_keys(value)
        time.sleep(5)

    @allure.suite("DepositSuite")
    @allure.description("Close deposit")
    @allure.tag("Testrail C2")
    @pytestrail.case("C2")
    def test_close_deposit(self):
        pass

    @allure.suite("DepositSuite")
    @allure.description("Change deposit term and currency value")
    @allure.tag("Testrail C7")
    @pytestrail.case("C7")
    @pytest.mark.parametrize('currency_value, deposit_quantity',
                             [('RUB', 3), ('EUR', 3), ('USD', 1)])
    def test_change_deposit_term_and_currency(self, login, currency_value, deposit_quantity):
        date_value = '-1'
        deposit_type_value = '10'
        login.open_main_page()

        login.main_page.deposit_button_click()

        login.deposit_page.new_deposit_button_click()
        login.deposit_page.currency_radiobutton_click(currency_value)
        login.deposit_page.end_deposit_date_radiobutton_click(date_value)

        assert login.deposit_page.get_deposit_quantity(deposit_type_value) == deposit_quantity

    @allure.suite("DepositSuite")
    @allure.description("Open retirement deposit")
    @allure.tag("Testrail C8")
    @pytestrail.case("C8")
    # @pytest.mark.skip
    def test_open_pens_deposit(self, login):
        """
        Steps.
        1) Authorize
        2) Deposit tab
        3) Choose  currency
        4) Choose term
        5) Choose rate

        """
        login.open_main_page()

        login.main_page.deposit_button_click()

        login.deposit_page.new_deposit_button_click()
        login.deposit_page.open_pens_deposit_button_click()

        assert login.deposit_page.alert_label_get_text() == DepositPageConstants.PENS_ALERT_TEXT
