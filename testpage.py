from BaseApp import BasePage


class OperationsHelper(BasePage):
    def enter_username(self, username):
        self.enter_text_into_field(self.locators["LOCATOR_USERNAME"], username, description="Username")

    def enter_pass(self, password):
        self.enter_text_into_field(self.locators["LOCATOR_PASS"], password, description="Password")

    def click_login_btn(self):
        self.click_button(self.locators["LOCATOR_BTN_LOGIN"], description="Login button")

    def get_msg(self):
        return self.get_text_from_element(self.locators["LOCATOR_ERR_MSG"], description="Error message")

    def get_auth_text(self):
        return self.get_text_from_element(self.locators["LOCATOR_AUTH_MSG"], description="Authenticate message")
