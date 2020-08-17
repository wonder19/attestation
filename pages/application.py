import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.deposit import DepositPage
from pages.login import LoginPage
from pages.main import MainPage

logger = logging.getLogger()


class Application:
    def __init__(self, base_url, headless):
        driver_path = ChromeDriverManager().install()
        options: Options = Options()
        options.headless = headless
        self.wd = webdriver.Chrome(driver_path, options=options)
        self.base_url = base_url
        self.login_page = LoginPage(self)
        self.main_page = MainPage(self)
        self.deposit_page = DepositPage(self)

    def open_main_page(self):
        logger.info('Open main page')
        self.wd.get(self.base_url + "welcome")

    def open_deposit_condition_confirm_pae(self, value:str):
        self.wd.get(self.base_url + value)
