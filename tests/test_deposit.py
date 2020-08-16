import time

import allure
import pytest
from pytest_testrail.plugin import pytestrail

from common.constants import DepositPageConstants


@allure.suite("DepositSuite")
@allure.description("Open Deposit test")
@allure.tag("Testrail C1")
@pytestrail.case("C1")
# @pytest.mark.parametrize('currency_value', 'date_value',
#                          [('RUB', 'USD', ' EUR'),
#                          ('15', '31', '91')])
def test_open_deposit(login):
    """
    Steps.
    1) Authorize
    2) Deposit tab
    3) Choose  currency
    4) Choose term
    5) Chose rate
    6) Input summ
    7) Click continue button
    8) Accept conditions
    9) Click continue button
    """
    currency_value = 'RUB'
    date_value = '15'
    login.open_main_page()

    login.main_page.deposit_button_click()
    login.deposit_page.new_deposit_button_click()
    login.deposit_page.fill_deposit_condition(currency_value, date_value)


@allure.suite("DepositSuite")
def test_close_deposit():
    pass


@allure.suite("DepositSuite")
def test_change_deposit_currency():
    pass


@allure.suite("DepositSuite")
def test_change_deposit_term():
    pass


@allure.suite("DepositSuite")
def test_open_pens_deposit(login):
    """
    Steps.
    1) Authorize
    2) Deposit tab
    3) Choose  currency
    4) Choose term
    5) Chose rate

    """

    login.open_main_page()

    login.main_page.deposit_button_click()

    login.deposit_page.new_deposit_button_click()
    login.deposit_page.open_pens_deposit_button_click()

    assert login.deposit_page.alert_label_get_text() == DepositPageConstants.PENS_ALERT_TEXT
