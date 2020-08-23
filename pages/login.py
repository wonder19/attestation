import logging

from locators.login import LoginLocators
from model.login import UserData

logger = logging.getLogger()


class LoginPage:
    def __init__(self, app):
        self.app = app

    def email_input(self):
        return self.app.wd.find_element(*LoginLocators.LOGIN)

    def password_input(self):
        return self.app.wd.find_element(*LoginLocators.PASSWORD)

    def login_button(self):
        return self.app.wd.find_element(*LoginLocators.LOGIN_BUTTON)

    def login_opt_button(self):
        return self.app.wd.find_element(*LoginLocators.LOGIN_OPT_BUTTON)

    def auth(self, user_data: UserData, is_submit=True):
        """
        :param user_data: Class UserData, attribuites (Login: str, Password: str)
        :param is_submit: Attribuit, Boolean
        """
        logger.info('Autorized user')
        if user_data.login is None:
            self.email_input().send_keys(user_data.login)
        if user_data.password is None:
            self.password_input().send_keys(user_data.password)
        if is_submit:
            self.login_button().click()
        self.login_opt_button().click()
