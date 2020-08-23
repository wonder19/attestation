from selenium.webdriver.common.by import By


class DepositLocators:
    NEW_DEPOSIT_BUTTON = (By.ID, "btn-show-rates")
    OPEN_PENS_DEPOSIT_BUTTON = (By.XPATH, '//*[@id="table-deposit-rates"]/tbody/tr[6]/td[7]/a')
    END_DATE_INPUT = (By.ID, 'endDate')
    AMOUNT_INPUT = (By.ID, 'amount')
    CURRENCY_EUR_INPUT = (By.XPATH, '//*[@id="deposit-rates"]/div[1]/div[1]/label[2]/input')
    DEPOSIT_TERM = (By.NAME, "minDays")
    RATE_LABEL = (By.CLASS_NAME, 'hidden')
    CONDITION_CHECKBOX = (By.NAME, 'condition.newDepositConditions')
    ALERT_LABEL = (By.XPATH, '//*[@id="alerts-container"]/div[2]')
    SUBMIT_BUTTON = (By.ID, 'submit-button')
