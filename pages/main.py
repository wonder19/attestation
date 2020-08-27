import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from locators.main import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, app):
        self.app = app
        self.wait = WebDriverWait(self.app.wd, 10)

    def deposit_button(self):
        return self.app.wd.find_element(*MainPageLocators.DEPOSIT)

    def deposit_button_click(self):
        self.deposit_button().click()

    def cards_button(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(MainPageLocators.CARD))
        except NoSuchElementException:
            time.sleep(5)
            return self.wait.until(EC.visibility_of_element_located(MainPageLocators.CARD))

    def cards_button_click(self):
        self.cards_button().click()

    def logout_button(self):
        return self.wait.until(EC.visibility_of_element_located(MainPageLocators.LOGOUT_BUTTON))

    def logout_button_click(self):
        self.logout_button().click()

    def payment_button(self):
        return self.app.wd.find_element(*MainPageLocators.PAYMENT)

    def payment_button_click(self):
        self.payment_button().click()