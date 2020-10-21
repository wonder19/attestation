import logging
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import allure
from locators.deposit import DepositLocators
from model.deposit import DepositData

logger = logging.getLogger()


class DepositPage:
    def __init__(self, app):
        self.app = app
        self.wait = WebDriverWait(self.app.wd, 60)

    def currency_radiobutton(self, currency_value):
        return self.app.wd.find_element_by_xpath(
            ("//*[contains(text() ,'" + currency_value + "')]")
        )

    def currency_radiobutton_click(self, currency_value):
        logger.info("Choose deposit currency")
        self.currency_radiobutton(currency_value).click()

    def currency_eur_radiobutton(self):
        return self.app.wd.find_element(*DepositLocators.CURRENCY_EUR_INPUT)

    def currency_eur_radio_click(self):
        self.currency_eur_radiobutton().click()

    def end_deposit_date_radiobutton(self, date_value):
        return self.app.wd.find_element_by_xpath(
            (
                "//*[contains(@class, 'span6')]"
                "//*[contains(@value ,'" + date_value + "')]"
            )
        )

    def end_deposit_date_radiobutton_click(self, date_value):
        logger.info("Choose deposit end date")
        self.end_deposit_date_radiobutton(date_value).click()

    def get_deposit_quantity(self, value):
        deposits = self.app.wd.find_elements_by_xpath(
            (
                "//*[contains(@data-rate-id ,'"
                + value
                + "')]//*[contains(@class, 'place-deposit')]"
            )
        )
        return len(deposits)

    def new_deposit_button(self):
        return self.app.wd.find_element(*DepositLocators.NEW_DEPOSIT_BUTTON)

    @allure.step("Start new deposit opening process")
    def new_deposit_button_click(self):
        logger.info("Start new deposit opening process")
        self.new_deposit_button().click()

    def open_deposit_button(self, value: str):
        return self.app.wd.find_element_by_xpath(
            (
                "//*[contains(@data-rate-id ,'"
                + value
                + "')]//*[contains(@class, 'place-deposit')]"
            )
        )

    def open_deposit_button_click(self, value):
        logger.info("Select deposit type")
        self.open_deposit_button(value).click()

    def open_pens_deposit_button(self):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(DepositLocators.AMOUNT_INPUT)
            )
        except NoSuchElementException:
            logger.error("NoSuchElementException")

    def open_pens_deposit_button_click(self):
        logger.info("Open retirement deposit")
        self.open_pens_deposit_button().click()

    def alert_label(self):
        return self.app.wd.find_element(*DepositLocators.ALERT_LABEL)

    @allure.step("Show alert text")
    def alert_label_get_text(self):
        logger.info("Show alert text")
        return self.alert_label().text

    @allure.step("Fill deposit condition")
    def fill_deposit_condition(self, deposit_data: DepositData):
        """
        Function for input deposit options.
        :param deposit_data:
        :param currency_value:
        :param date_value:
        :param deposit_type:
        :return:
        """
        logger.info("Fill deposit conditions")
        self.currency_radiobutton_click(deposit_data.currency)
        self.end_deposit_date_radiobutton_click(deposit_data.end_date)
        self.open_deposit_button_click(deposit_data.deposit_type)

    def deposit_condition(self, deposit_data: DepositData):
        self.app.main_page.deposit_button_click()
        self.app.deposit_page.new_deposit_button_click()
        self.app.deposit_page.fill_deposit_condition(deposit_data)

    def end_deposit_date_input(self):
        return self.wait.until(
            EC.visibility_of_element_located(DepositLocators.END_DATE_INPUT)
        )

    def end_deposit_date_input_send_keys(self, value):
        logger.info("Fill deposit end date")
        self.end_deposit_date_input().send_keys(value)

    def amount_input(self):
        return self.app.wd.find_element(*DepositLocators.END_DATE_INPUT)

    def amount_input_send_keys(self, amount):
        logger.info("Fill deposit amount")
        self.open_pens_deposit_button().send_keys(amount)

    def get_confirm_condition_page_text(self, deposit_type):

        self.open_pens_deposit_button(deposit_type).get_attribute("href")

    def submit_button(self):
        return self.app.wd.find_element(*DepositLocators.SUBMIT_BUTTON)

    def submit_button_click(self):
        logger.info("Open deposit")
        self.submit_button().click()

    def new_deposit_condition_checkbox(self):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(DepositLocators.CONDITION_CHECKBOX)
            )
        except NoSuchElementException:
            logger.error("NoSuchElementException")

    def new_deposit_condition_checkbox_click(self):
        self.new_deposit_condition_checkbox().click()

    def confirm_button(self):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(DepositLocators.CONFIRM_BUTTON)
            )
        except NoSuchElementException:
            logger.error("NoSuchElementException")

    def confirm_button_click(self):
        self.confirm_button().click()

    def deposit_success_alert(self):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(DepositLocators.DEPOSIT_ALERT_SUCCESS)
            )
        except NoSuchElementException:
            logger.error("NoSuchElementException")

    def deposit_success_alert_get_text(self):
        return self.deposit_success_alert().text
