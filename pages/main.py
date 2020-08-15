from locators.main import MainPageLocators


class MainPage:
    def __init__(self, app):
        self.app = app

    def deposit_button(self):
        return self.app.wd.find_element(*MainPageLocators.DEPOSIT)

    def deposit_button_click(self):
        self.deposit_button().click()

    def greeting_label(self):
        return self.app.wd.find_element(*MainPageLocators.GREETING)

