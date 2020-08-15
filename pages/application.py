from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from common.logging import setup
from common.utils import logging as log
from pages.login import LoginPage
from pages.main import MainPage
import logging

logger = logging.getLogger()

class Application:
    def __init__(self, base_url, headless):
        setup('INFO')
        logger.setLevel('INFO')
        driver_path = ChromeDriverManager().install()
        options: Options = Options()
        options.headless = headless
        self.wd = webdriver.Chrome(driver_path, options=options)
        self.base_url = base_url
        self.login_page = LoginPage(self)
        self.main_page = MainPage(self)

    @log('Open main page')
    def open_main_page(self):
        self.wd.get(self.base_url + 'welcome')