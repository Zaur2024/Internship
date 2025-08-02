from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):
    # Locator for the "Secondary" option in the left menu
    secondary_option = (By.CSS_SELECTOR, 'a[href="/secondary-listings"]')


    def open(self, url="https://soft.reelly.io"):
        self.open_url(url)

    def click_secondary(self):
        # Wait until it's clickable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.secondary_option)
        )
        # Find it again (fresh) after it's confirmed clickable
        element = self.find_element(*self.secondary_option)

        # Scroll into view to make sure it's visible
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        # Take screenshot before clicking
        self.driver.save_screenshot("before_click_secondary.png")

        element.click()
        # Finally, click the element