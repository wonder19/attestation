import logging
import time

import allure

from locators.deposit import DepositLocators
from model.deposit import DepositData

logger = logging.getLogger()


class DepositPage:
    def __init__(self, app):
        self.app = app

    def currency_radiobutton(self, currency_value):
        return self.app.wd.find_element_by_xpath(("//*[contains(text() ,'" + currency_value + "')]"))

    def currency_radiobutton_click(self, currency_value):
        self.currency_radiobutton(currency_value).click()

    def currency_eur_radiobutton(self):
        return self.app.wd.find_element(*DepositLocators.CURRENCY_EUR_INPUT)

    def currency_eur_radio_click(self):
        self.currency_eur_radiobutton().click()

    def end_deposit_date_radiobutton(self, date_value):
        return self.app.wd.find_element_by_xpath(("//*[contains(@class, 'span6')]"
                                                  "//*[contains(@value ,'" + date_value + "')]"))

    def end_deposit_date_radiobutton_click(self, date_value):
        self.end_deposit_date_radiobutton(date_value).click()

    def get_deposit_quantity(self, value):
        deposits = self.app.wd.find_elements_by_xpath(("//*[contains(@data-rate-id ,'" + value + "')]"
                                                                                                 "//*[contains(@class, 'place-deposit')]"))
        return len(deposits)

    # def rate_label(self):
    #     return self.app.wd.find_element(*DepositLocators.RATE_LABEL)
    #
    # @allure.step('Show rate')
    # def rate_label_text(self):
    #     return self.rate_label().text

    def new_deposit_button(self):
        return self.app.wd.find_element(*DepositLocators.NEW_DEPOSIT_BUTTON)

    @allure.step('Start new deposit opening process')
    def new_deposit_button_click(self):
        self.new_deposit_button().click()

    def open_deposit_button(self, value: str):
        return self.app.wd.find_element_by_xpath(("//*[contains(@data-rate-id ,'" + value + "')]"
                                                                                            "//*[contains(@class, 'place-deposit')]"))

    def open_deposit_button_click(self, value):
        self.open_deposit_button(value).click()

    def open_pens_deposit_button(self):
        return self.app.wd.find_element(*DepositLocators.OPEN_PENS_DEPOSIT_BUTTON)

    def open_pens_deposit_button_click(self):
        self.open_pens_deposit_button().click()

    def alert_label(self):
        return self.app.wd.find_element(*DepositLocators.ALERT_LABEL)

    @allure.step('Show alert text')
    def alert_label_get_text(self):
        return self.alert_label().text

    @allure.step('Fill deposit condition')
    def fill_deposit_condition(self, deposit_data: DepositData):
        """
        Function for input deposit options.
        :param currency_value:
        :param date_value:
        :param deposit_type:
        :return:
        """
        logger.info('Fill deposit conditions')
        self.currency_radiobutton_click(deposit_data.currency)
        self.end_deposit_date_radiobutton_click(deposit_data.end_date)
        self.open_deposit_button_click(deposit_data.deposit_type)
        return self.open_pens_deposit_button(deposit_data.deposit_type).get_attribute("href")

    def end_deposit_date_input(self):
        return self.app.wd.find_element(*DepositLocators.END_DATE_INPUT)

    def end_deposit_date_input_send_keys(self):
        self.open_pens_deposit_button().send_keys()

    def amount_input(self):
        return self.app.wd.find_element(*DepositLocators.END_DATE_INPUT)

    def amount_input_send_keys(self):
        self.open_pens_deposit_button().send_keys()

    def get_confirm_condition_page_text(self, deposit_type):
        self.open_pens_deposit_button(deposit_type).get_attribute("href")