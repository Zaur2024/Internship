from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class loginPage(BasePage):
    # Locators
    email_input = (By.CSS_SELECTOR,'[wized="emailInput"]')
    password_input = (By.CSS_SELECTOR,'[wized="passwordInput"]')
    login_button = (By.CSS_SELECTOR,".login-button.w-button")

    def login(self, email, password):
        self.send_keys(self.email_input, email)
        self.send_keys(self.password_input, password)
        self.click(self.login_button)