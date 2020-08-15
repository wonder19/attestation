from selenium.webdriver.common.by import By


class LoginLocators:
    LOGIN = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    LOGIN_OPT_BUTTON = (By.ID, "login-otp-button")
