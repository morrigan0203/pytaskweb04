from BaseApp import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
import logging
import time


class OperationsContactUsHelper(BasePage):
    def open_contact_us_page(self):
        self.go_to_site('https://test-stand.gb.ru/contact')

    def fill_contact_us(self, your_name=None, your_email=None, content=None):
        logging.info(f'Fill contact us form : {your_name} {your_email} {content}')

        if your_name:
            time.sleep(0.5)
            self.enter_text_into_field(self.locators["LOCATOR_YOUR_NAME"], your_name, description="Your name")

        if your_email:
            time.sleep(0.5)
            self.enter_text_into_field(self.locators["LOCATOR_YOUR_EMAIL"], your_email, description="Your email")

        if content:
            time.sleep(0.5)
            self.enter_text_into_field(self.locators["LOCATOR_CONTENT"], content, description="Content")

        time.sleep(0.5)
        self.click_button(self.locators["LOCATOR_BTN"], description="Send Btn")

    def get_alert_msg(self, wait_time):
        alert = WebDriverWait(self.driver, wait_time).until(EC.alert_is_present(), message=f"Can't find alert")
        msg = alert.text
        alert.accept()
        return msg

    def check_alert_not_present(self, wait_time):
        try:
            WebDriverWait(self.driver, wait_time).until(EC.alert_is_present(), message=f"Can't find alert")
            return False
        except (NoAlertPresentException, TimeoutException):
            return True

    def check_email_label_red(self):
        email_label_color = self.get_element_property(self.locators["LOCATOR_EMAIL_LABEL"], "color")
        return "rgba(183, 28, 28, 1)" == email_label_color
