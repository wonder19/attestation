import logging
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.payment import PaymentLocators
from model.payment import PaymentData

logger = logging.getLogger()


class PaymentPage:

    def __init__(self, app):
        self.app = app
        self.wait = WebDriverWait(self.app.wd, 30)

    def smart_payment_input(self):
        return self.app.wd.find_element(*PaymentLocators.SMART_PAYMENT)

    def smart_payment_input_set_text(self, input_value):
        logger.info('Fill value for smart payment')
        self.smart_payment_input().send_keys(input_value)

    def between_wallets_link(self):
        return self.app.wd.find_element(*PaymentLocators.BETWEEN_WALLETS)

    def between_wallets_link_click(self):
        logger.info('Select between wallets payment type')
        self.between_wallets_link().click()

    def smart_payment_dropdown_value(self):
        return self.app.wd.find_element(*PaymentLocators.DROPDOWN_VALUE)

    def smart_payment_dropdown_value_get_text(self):
        logger.info('Select smart payment value')
        return self.smart_payment_dropdown_value().text.lower()

    def continue_button(self):
        return self.app.wd.find_element(*PaymentLocators.FORWARD)

    def continue_button_click(self):
        logger.info('Continue process of payment creation')
        self.continue_button().click()

    def empty_fields_alert_label(self):
        return self.wait.until(EC.visibility_of_element_located(PaymentLocators.ALERT))

    def empty_fields_alert_label_get_text(self):
        logger.info('Show alert if fields are empty')
        return self.empty_fields_alert_label().text

    def payment_date_input(self):
        return self.app.wd.find_elements(*PaymentLocators.PAYMENT_DATE)

    def payment_date_input_set_text(self, payment_date):
        logger.info('Fill payment date')
        self.payment_date_input().send_keys(payment_date)

    def amount_input(self):
        return self.app.wd.find_element(*PaymentLocators.PAYMENT_AMOUNT)

    def amount_input_set_text(self, amount_value):
        logger.info('Fill payment amount')
        self.amount_input().send_keys(amount_value)

    def comment_input(self):
        return self.app.wd.find_element(*PaymentLocators.PAYMENT_COMMENT)

    def fill_payment_inputs(self, payment_data: PaymentData):
        logger.info('Fill payment conditions')
        self.amount_input().send_keys(payment_data.amount)
        self.comment_input().send_keys(payment_data.comment)
        # self.payment_date_input()[2].click()
        self.continue_button_click()

    def on_card_payment_link(self):
        return self.app.wd.find_element(*PaymentLocators.CARD_PAYMENTS)

    def on_card_payment_link_click(self):
        logger.info('Select card payment type')
        self.on_card_payment_link().click()

    def card_payment_amount(self):
        return self.app.wd.find_element(*PaymentLocators.CARD_PAYMENTS_AMOUNT)

    def card_payment_amount_set_text(self, amount_value):
        logger.info('Fill payment amount')
        self.card_payment_amount().send_keys(amount_value)

    def card_error_alert(self):
        try:
            time.sleep(5)
            return self.wait.until(EC.visibility_of_element_located(PaymentLocators.CARD_ERROR_ALERT))
        except:
            time.sleep(5)
            return self.wait.until(EC.visibility_of_element_located(PaymentLocators.CARD_ERROR_ALERT))

    def card_error_alert_get_text(self):
        logger.info('Show alert for card payment')
        return self.card_error_alert().text

    def recipient_card(self):
        return self.app.wd.find_element(*PaymentLocators.RECIPIENT_CARD)

    def select_recipient_card(self, card_value):
        logger.info('Select recipient card')
        Select(self.recipient_card()).select_by_value(card_value)

    def card_payment_demo_alert(self):
        return self.wait.until(EC.visibility_of_element_located(PaymentLocators.CARD_PAYMENT_DEMO_ALERT))

    def card_payment_demo_alert_get_text(self):
        logger.info('Show alert for card payment')
        return self.card_payment_demo_alert().text

    def payment_request_link(self):
        return self.app.wd.find_element(*PaymentLocators.PAYMENT_REQUEST_LINK)

    def payment_request_link_click(self):
        logger.info('Select request payment type')
        self.payment_request_link().click()

    def payment_request_amount_input(self):
        return self.app.wd.find_element(*PaymentLocators.PAYMENT_REQUEST_AMOUNT)

    def payment_request_comment_input(self):
        return self.app.wd.find_element(*PaymentLocators.PAYMENT_REQUEST_COMMENT)

    def fill_payment_request_values(self, payment_data: PaymentData):
        logger.info('Fill request payment type values')
        self.payment_request_amount_input().send_keys(payment_data.amount)
        self.payment_request_comment_input().send_keys(payment_data.comment)
        self.continue_button_click()

    def payment_request_popup(self):
        return self.app.wd.find_element(*PaymentLocators.PAYMENT_REQUEST_POPUP)

    def payment_request_popup_close_button(self):
        return self.app.wd.find_element(*PaymentLocators.PAYMENT_REQUEST_POPUP_CLOSE_BUTTON)

    def payment_request_popup_close_button_click(self):
        logger.info('Close request payment popup')
        self.payment_request_popup_close_button().click()

    def payment_success_alert(self):
        return self.app.wd.find_element(*PaymentLocators.PAYMENT_ALERT_SUCCESS)

    def payment_success_alert_get_text(self):
        logger.info('Show success message')
        return self.payment_success_alert().text

    def get_request_quantity(self):
        quantity = self.app.wd.find_elements(*PaymentLocators.PAYMENT_REQUEST)
        return len(quantity)
