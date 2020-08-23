import os
import time
from datetime import datetime

import allure
import pytest

from model.deposit import DepositData
from model.login import UserData
from pages.application import Application


@pytest.fixture(scope="session")
def app(request):
    base_url = request.config.getoption("--base-url")
    headless = request.config.getoption("--headless")
    fixture = Application(base_url, headless)
    fixture.wd.implicitly_wait(10)
    fixture.wd.maximize_window()
    yield fixture
    fixture.wd.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="launching browser without gui",
    ),
    parser.addoption(
        "--base-url",
        action="store",
        default="https://idemo.bspb.ru/",
        help="enter base_url",
    ),
    parser.addoption(
        "--username", action="store", default="demo", help="enter username",
    ),
    parser.addoption(
        "--password", action="store", default="demo", help="enter password",
    )


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', p)
)


@pytest.fixture(scope="module")
def login(app, request):
    app.open_main_page()
    login = request.config.getoption("--username")
    password = request.config.getoption("--password")
    user_data = UserData(login=login, password=password)
    app.login_page.auth(user_data)
    yield app
    app.open_main_page()
    app.main_page.logout_button_click()

@pytest.fixture(scope="module")
def fill_deposit_condition(app):
    deposit_data = DepositData().random()
    app.main_page.deposit_button_click()
    app.deposit_page.new_deposit_button_click()
    url=app.deposit_page.fill_deposit_condition(deposit_data)
    app.open_deposit_condition_confirm_page(url)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        try:
            with open("failures", mode) as f:
                if "app" in item.fixturenames:
                    web_driver = item.funcargs["app"]
                else:
                    print("Fail to take screen-shot")
                    return
            allure.attach(
                web_driver.wd.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception as e:
            print("Fail to take screen-shot: {}".format(e))
