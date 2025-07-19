from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):
    # Locator for the "Secondary" option in the left menu
    secondary_option = (By.CSS_SELECTOR, 'a[href="/secondary-listings"]')


    def open(self, url="https://soft.reelly.io"):
        self.open_url(url)

    def click_secondary(self):
        self.click(self.secondary_option)