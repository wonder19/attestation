import time

import allure

from locators.deposit import DepositLocators


class DepositPage:
    def __init__(self, app):
        self.app = app

    def currency_input(self, i):
        return self.app.wd.find_element(*DepositLocators.CURENCY_INPUT)

    @allure.step('Input currency value')
    def currency_input_value(self, value):
        self.currency_input().setAttribute('value', value)

    def end_date_input(self):
        return self.app.wd.find_element(*DepositLocators.END_DATE_INPUT)

    # def end_date_input_value(self, value):
    #     self.end_date_input().send_keys(value)
    def end_date_input_value(self, value):
        self.end_date_input().setAttribute('value', value)

    def new_deposit_button(self):
        return self.app.wd.find_element(*DepositLocators.NEW_DEPOSIT_BUTTON)

    @allure.step('Start new deposit opening process')
    def new_deposit_button_click(self):
        self.new_deposit_button().click()

    def open_deposit_button(self):
        return self.app.wd.find_element(*DepositLocators.OPEN_DEPOSIT_BUTTON)

    def open_deposit_button_click(self):
        self.open_deposit_button().click()

    def open_pens_deposit_button(self):
        return self.app.wd.find_element(*DepositLocators.OPEN_PENS_DEPOSIT_BUTTON)

    def open_pens_deposit_button_click(self):
        self.open_pens_deposit_button().click()

    def alert_label(self):
        return self.app.wd.find_element(*DepositLocators.ALERT_LABEL)

    @allure.step('Show alert text')
    def alert_label_get_text(self):
        return self.alert_label().text


    def fill_deposit_condition(self, currency_value: str,
                               date_value):
        """

        :param currency_value:
        :param date_value:
        :return:
        """
        self.currency_input_value(value=currency_value)
        self.end_date_input_value(value=date_value)
        time.sleep(5)
        self.open_deposit_button_click()

