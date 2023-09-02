from BaseApp import BasePage
import logging
import time


class OperationsAddPost(BasePage):
    def add_post(self):
        time.sleep(0.5)
        self.click_button(self.locators["LOCATOR_ADD_POST"], description="Add Post btn")

    def post_content(self, title=None, descr=None, content=None):
        logging.info(f'Fill post {title} {descr} {content}')

        if title:
            time.sleep(0.5)
            self.enter_text_into_field(self.locators["LOCATOR_POST_TITLE"], title, description="Title")

        if descr:
            time.sleep(0.5)
            self.enter_text_into_field(self.locators["LOCATOR_POST_DESCR"], descr, description="Description")

        if content:
            time.sleep(0.5)
            self.enter_text_into_field(self.locators["LOCATOR_POST_CONTENT"], content, description="Content")

        time.sleep(0.5)
        self.find_element(self.locators["LOCATOR_POST_CREATE_BTN"]).click()

    def find_post(self):
        time.sleep(0.5)
        return self.get_text_from_element(self.locators["LOCATOR_TITLE_NEW_POST"], description="Title of new post")

