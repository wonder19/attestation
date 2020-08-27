from selenium.webdriver.common.by import By


class CardLocators:
    ORDER_NEW_CARD = (By.ID, 'order-new-card-link')
    TYPE_SELECTOR = (By.CSS_SELECTOR, '#type-select')
    ORDER_NEW_VIRTUAL_CARD = (By.XPATH, '//*[@id="card-0"]/div/div[2]/div[3]/a')
    MONTHLY_INCOME = (By.XPATH, '//*[@id="application-inputs"]/div[5]/div/div/input')
    CREDIT_HISTORY = (By.NAME, 'condition.creditHistory')
    PERSONAL_DATA = (By.NAME, 'condition.personalDataProcessing')
    MOBILE_SUBSCRIBE = (By.NAME, 'condition.mobileSubscriberDataProcessing')
    VIRTUAL_CONDITION = (By.NAME, 'condition.virtualConditions')
    INSPECT_BUTTON = (By.ID, 'inspect')
    SUBMIT_BUTTON = (By.ID, 'submit-button')
    CONFIRM_BUTTON = (By.XPATH, '//*[@id="confirm"]')
    SMS_CODE_INPUT = (By.NAME, 'otpCode')
    ERROR_LABEL = (By.CLASS_NAME, 'error')
    IFRAME = (By.XPATH, '//*[@id="confirmation-frame"]')
    SUCSESS_TITLE = (By.XPATH, '//*[@id="contentbar"]/div[1]/h1')
    CREDIT_CARD_LINK = (By.ID, 'offer-for-card')
    OFFICE = (By.XPATH, '//*[@id="card-branch"]')
    DEBET_CARD_OFFICE = (By.ID, 'card-branch')
    FORWARD = (By.ID, 'forward')
    CARD_ALERT_SUCCESS = (By.XPATH, '//*[@class="alert alert-success"]')

