from selenium.webdriver.common.by import By

from common.constants import DepositPageConstants


class DepositLocators:
    NEW_DEPOSIT_BUTTON = (By.ID, "btn-show-rates")
    # OPEN_DEPOSIT_BUTTON = (By.LINK_TEXT, "deposits/form/10139?days=367")
    OPEN_DEPOSIT_BUTTON = (By.XPATH, '//*[@id="table-deposit-rates"]/tbody/tr[1]/td[7]/a')
    OPEN_PENS_DEPOSIT_BUTTON=(By.XPATH,'//*[@id="table-deposit-rates"]/tbody/tr[6]/td[7]/a')
    END_DATE_INPUT = (By.XPATH, '//*[@id="deposit-rates"]/div[1]/div[2]/div[3]/label[1]/input')
    # END_DATE_INPUT = (By.ID, "endDate")
    AMOUNT_INPUT = (By.ID, "amount")
    CURENCY_INPUT = (By.NAME, DepositPageConstants.CURRENCY_PATH)
    DEPOSIT_TERM = (By.NAME, "minDays")
    RATE_LABEL = (By.CLASS_NAME, 'hidden')
    CONDITION_CHECKBOX = (By.NAME, 'condition.newDepositConditions')
    ALERT_LABEL=(By.XPATH, '//*[@id="alerts-container"]/div[2]')
