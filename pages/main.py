from locators.main import MainPageLocators


class MainPage:
    def __init__(self, app):
        self.app = app

    def deposit_button(self):
        return self.app.wd.find_element(*MainPageLocators.DEPOSIT)

    def deposit_button_click(self):
        self.deposit_button().click()

    def cards_button(self):
        return self.app.wd.find_element(*MainPageLocators.CARD)

    def cards_button_click(self):
        self.cards_button().click()

    def logout_button(self):
        return self.app.wd.find_element(*MainPageLocators.LOGOUT_BUTTON)

    def logout_button_click(self):
        self.logout_button().click()

    def payment_button(self):
        return self.app.wd.find_element(*MainPageLocators.PAYMENT)

    def payment_button_click(self):
        self.payment_button().click()