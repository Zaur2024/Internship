from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
class MainPage(BasePage):
    # Locator for the "Secondary" option in the left menu
    secondary_option = (By.CSS_SELECTOR, 'a[href="/secondary-listings"]')


    def open(self, url="https://soft.reelly.io"):
        self.open_url(url)

    def click_secondary(self):
        sleep(2)
        WebDriverWait(self.driver, timeout=20).until(
            EC.element_to_be_clickable(self.secondary_option)
        )

        element = self.find_element(*self.secondary_option)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.save_screenshot("before_click_secondary.png")
        element.click()  # Actually click the element here