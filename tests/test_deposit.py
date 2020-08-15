import allure
import pytest
from pytest_testrail.plugin import pytestrail


@allure.suite("DepositSuite")
@allure.description("Open Deposit test")
@allure.tag("Testrail C1")
@pytest.mark.skip
@pytestrail.case("C1")
def test_open_deposit(login):
    """
    Steps.
    1) Authorize
    2) Deposit tab
    3) Choose  curency
    """
    login.open_main_page()
    login.main_page.deposit_button_click()
