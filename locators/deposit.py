from selenium.webdriver.common.by import By


class Deposit:
    NEW_DEPOSIT_BUTTON=(By.ID, 'new-deposit-btn')
    OPEN_DEPOSIT_BUTTON=(By.LINK_TEXT, 'deposits/form/10139?days=367')
    END_DATE_INPUT=(By.ID, 'endDate')
    AMOUNT_INPUT=(By.ID, 'amount')
    CURENCY_INPUT =(By.NAME, 'currency')
    DEPOSIT_TERM = (By.NAME, 'minDays')



