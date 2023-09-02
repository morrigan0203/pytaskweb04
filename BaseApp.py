from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
import yaml


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.locators = dict()
        with open("./locators.yaml") as f:
            locators = yaml.safe_load(f)
        for locator in locators["xpath"].keys():
            self.locators[locator] = (By.XPATH, locators["xpath"][locator])
        for locator in locators["css"].keys():
            self.locators[locator] = (By.CSS_SELECTOR, locators["css"][locator])

    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                             message=f"Can't find element by locator {locator}")
        except:
            logging.exception("Find element exception")
            element = None
        return element

    def get_element_property(self, locator, prop):
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(prop)
        logging.error(f'Property {prop} not found in element with locator {locator}')
        return None

    def go_to_site(self, site='http://test-stand.gb.ru'):
        try:
            start_browser = self.driver.get(site)
        except:
            logging.exception("Exception with open site")
            start_browser = None
        return start_browser

    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f'Send {word} to element {element_name}')
        field = self.find_element(locator)
        if not field:
            logging.error(f'Element {element_name} not fount')
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f'Exception while operation with {element_name}')
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f'Click to element {element_name}')
        field = self.find_element(locator)
        if not field:
            logging.error(f'Element {element_name} not fount')
            return False
        try:
            field.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f'Clicked {element_name} button')
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f'Click to element {element_name}')
        field = self.find_element(locator, time=3)
        if not field:
            logging.error(f'Element {element_name} not fount')
            return None
        try:
            text = field.text
        except:
            logging.exception(f'Exception while get text from {element_name}')
            return None
        logging.debug(f'We found text {text} in field {element_name}')
        return text
