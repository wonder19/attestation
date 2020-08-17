from selenium.webdriver.common.by import By


class CardLocators:
    ORDER_NEW_CARD = (By.ID, 'order-new-card-link')
    MONTHLY_INCOME = (By.NAME, 'application.monthlyIncome')
    CREDIT_HISTORY = (By.NAME, 'condition.creditHistory')
    PERSONAL_DATA = (By.NAME, 'condition.personalDataProcessing')
    MOBILE_SUBSCRIBE = (By.NAME, 'condition.mobileSubscriberDataProcessing')
    INSPECT_BUTTON = (By.ID, 'inspect')
