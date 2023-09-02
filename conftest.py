import logging
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from gb import auth


with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

browser_ = testdata["browser"]


@pytest.fixture(scope="session")
def browser():
    logging.info(f'Browser : {browser_}')
    if browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def incorrect_word():
    return "babt"


@pytest.fixture()
def correct_word():
    return "baby"


@pytest.fixture()
def authorization():
    return auth()


@pytest.fixture()
def new_title():
    return "new_title"


@pytest.fixture()
def new_description():
    return "new_description"


