from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException, TimeoutException, NoSuchElementException

class MainPage(BasePage):
    # Locator for the "Secondary" option in the left menu
    off_plan_option = (By.CSS_SELECTOR, '[wized="newOffPlanLink"]')
    secondary_option = (By.CSS_SELECTOR, 'a[href="/secondary-listings"]')

    # Example locator for a possible modal popup close button (adjust if needed)
    modal_close_button = (By.CSS_SELECTOR, '.popup-close, .modal-close, .close-button')

    def open(self, url="https://soft.reelly.io"):
        self.open_url(url)

    def handle_popups(self):
        # Handle browser alert popups
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
            print("Alert popup accepted.")
        except NoAlertPresentException:
            print("No alert popup present.")
        except Exception as e:
            print(f"Unexpected error handling alert: {e}")

        # Handle possible HTML modal popups with close buttons
        try:
            modal_close = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.modal_close_button)
            )
            modal_close.click()
            print("Modal popup closed.")
        except (TimeoutException, NoSuchElementException):
            print("No modal popup present or already closed.")
        except Exception as e:
            print(f"Unexpected error closing modal popup: {e}")

    def click_off_plan(self):
        # Wait longer for the element presence first
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(self.off_plan_option)
        )

        # Then wait for visibility and clickability
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.off_plan_option)
        )

        # Scroll into view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        # Optional: save screenshot before click for debugging
        self.driver.save_screenshot("off_plan_before_click.png")

        # Click the element (using JS click to avoid possible overlay issues)
        self.driver.execute_script("arguments[0].click();", element)

    def click_secondary(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.secondary_option)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
