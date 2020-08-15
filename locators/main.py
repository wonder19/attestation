from selenium.webdriver.common.by import By


class MainPageLocators:
    DEPOSIT = (By.ID, 'deposits')
    CREDIT = (By.ID, 'loans-index')
    CARD = (By.ID, 'cards-overview-index')
    PAYMENT = (By.ID, 'payments-form')
    LOGOUT_BUTTON = (By.ID, 'logout-button')
    GREETING = (By.ID, 'user-greeting')
