import logging
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from locators.card import CardLocators

logger = logging.getLogger()


class CardPage:
    def __init__(self, app):
        self.app = app
        self.wait = WebDriverWait(self.app.wd, 10)

    def order_new_card_button(self):
        return self.wait.until(EC.visibility_of_element_located(CardLocators.ORDER_NEW_CARD))

    def order_new_card_button_click(self):
        self.order_new_card_button().click()

    def new_debet_card_type_button(self, card_value: str):
        return self.app.wd.find_element_by_xpath(
            ("//*[contains(@data-ref ,'" + card_value + "')][@data-ga-product='debitcard']"))

    def new_debet_card_type_button_click(self, card_value: str):
        logger.info('Order new debet card with selected type')
        self.new_debet_card_type_button(card_value).click()

    def new_credit_card_type_button(self, card_value: str):
        return self.app.wd.find_element_by_xpath(
            ("//*[contains(@data-ref ,'" + card_value + "')][@data-ga-product='creditcard']"))

    def new_credit_card_type_button_click(self, card_value: str):
        logger.info('Order new credit card with selected type')
        self.new_credit_card_type_button(card_value).click()

    def new_virtual_card_type_button(self):
        return self.wait.until(EC.element_to_be_clickable(CardLocators.ORDER_NEW_VIRTUAL_CARD))

    def new_virtual_card_type_button_click(self):
        logger.info('Order new virtual card')
        self.new_virtual_card_type_button().click()

    def submit_button(self):
        return self.app.wd.find_element(*CardLocators.SUBMIT_BUTTON)

    def submit_button_click(self):
        self.submit_button().click()

    def virtual_condition_checkbox(self):
        return self.app.wd.find_element(*CardLocators.VIRTUAL_CONDITION)

    def virtual_condition_checkbox_click(self):
        logger.info('Click virtual condition checkbox')
        self.virtual_condition_checkbox().click()

    def sms_conformation(self, sms_code):
        logger.info('Input sms-code and confirm operation')
        try:
            self.wait.until(EC.frame_to_be_available_and_switch_to_it(CardLocators.IFRAME))
            time.sleep(5)
            self.wait.until(EC.visibility_of_element_located(CardLocators.SMS_CODE_INPUT)).clear()
            self.wait.until(EC.visibility_of_element_located(CardLocators.SMS_CODE_INPUT)).send_keys(sms_code)
            self.wait.until(EC.visibility_of_element_located(CardLocators.CONFIRM_BUTTON)).click()
            self.app.wd.switch_to.default_content()
        except NoSuchElementException:
            self.app.wd.find_element(*CardLocators.SMS_CODE_INPUT).send_keys(sms_code)
            self.app.wd.find_element(*CardLocators.CONFIRM_BUTTON).click()

    def error_label_get_text(self):
        logger.info('Show error text for incorrect sms-code')
        try:
            self.wait.until(EC.frame_to_be_available_and_switch_to_it(CardLocators.IFRAME))
            return self.app.wd.find_element(*CardLocators.ERROR_LABEL).text
        except NoSuchElementException:
            logger.error('NoSuchElementException')

    def success_title(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(CardLocators.ERROR_LABEL))
        except:
            return self.app.wd.find_element(*CardLocators.ERROR_LABEL)

    def success_title_get_text(self):
        logger.info('Show text for success title after card ordering')
        return self.success_title().text

    def type_card_dropdown(self):
        return self.app.wd.find_element(*CardLocators.TYPE_SELECTOR)

    def type_card_dropdown_select_value(self, card_type):
        logger.info('Select card type from dropdown')
        Select(self.type_card_dropdown()).select_by_value(card_type)

    def type_card_title_label(self, card_type: str):
        return self.app.wd.find_element_by_xpath("//*[contains(@data-tag,'" + card_type + "')]"
                                                                                          "//div[@class='span7']/h3")

    def type_card_title_label_get_text(self, card_type):
        logger.info('Show card type after sorting')
        return self.type_card_title_label(card_type).text

    def credit_card_link(self):
        return self.app.wd.find_element(*CardLocators.CREDIT_CARD_LINK)

    def credit_card_link_click(self):
        self.credit_card_link().click()

    def monthly_income_input(self):
        return self.wait.until(EC.visibility_of_element_located(CardLocators.MONTHLY_INCOME))

    def monthly_income_input_set_text(self, income_value):
        self.monthly_income_input().send_keys(income_value)

    def credit_history_checkbox(self):
        return self.wait.until(EC.visibility_of_element_located(CardLocators.CREDIT_HISTORY))

    def personal_data_checkbox(self):
        return self.wait.until(EC.visibility_of_element_located(CardLocators.PERSONAL_DATA))

    def mobile_subscribe_checkbox(self):
        return self.wait.until(EC.visibility_of_element_located(CardLocators.MOBILE_SUBSCRIBE))

    def inspect_credit_value_button(self):
        return self.wait.until(EC.visibility_of_element_located(CardLocators.INSPECT_BUTTON))

    def inspect_credit_value_button_click(self):
        self.inspect_credit_value_button().click()

    def fill_credit_card_information(self, income_value):
        time.sleep(5)
        self.monthly_income_input_set_text(income_value)
        self.credit_history_checkbox().click()
        self.personal_data_checkbox().click()
        self.mobile_subscribe_checkbox().click()

        self.inspect_credit_value_button_click()

    def office_selection_dropdown(self):
        return self.wait.until(EC.visibility_of_element_located(CardLocators.OFFICE))

    def office_selection_dropdown_input(self, office_value):
        Select(self.office_selection_dropdown()).select_by_value(office_value)

    def order_button(self):
        return self.app.wd.find_element(*CardLocators.FORWARD)

    def order_button_click(self):
        self.order_button().click()

    def card_success_alert(self):
        return self.wait.until(EC.visibility_of_element_located(CardLocators.CARD_ALERT_SUCCESS))

    def card_success_alert_get_text(self):
        return self.card_success_alert().text
