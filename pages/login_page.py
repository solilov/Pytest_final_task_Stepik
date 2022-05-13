from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.url in self.browser.current_url, 'Not in current url'

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM
        ), 'Login form is not found'

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM
        ), 'Register form is not found'

    def register_new_user(self, email, password):
        user_email = self.browser.find_element(*LoginPageLocators.EMAIL)
        user_email.send_keys(email)
        user_pass = self.browser.find_element(*LoginPageLocators.PASSWORD)
        user_pass.send_keys(password)
        confirm_pass = self.browser.find_element(*LoginPageLocators.CONF_PASSWORD)
        confirm_pass.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.BTN_REG)
        register_button.click()

    def user_login_to_account(self):
        assert self.is_element_present(
            *LoginPageLocators.LOG_OUT
        ), "User is not logged it"
