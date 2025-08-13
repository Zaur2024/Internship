from time import sleep
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage

class SecondaryDealsPage(BasePage):

    filters_button = (By.CSS_SELECTOR, '.filter-button')
    want_to_buy_checkbox = (By.CSS_SELECTOR, '[wized="ListingTypeBuy"]')
    apply_filter_button = (By.CSS_SELECTOR, '[wized="applyFilterButtonMLS"]')
    deal_tags = (By.CSS_SELECTOR, '[wized="saleTagMLS"]')

    def click_filters(self):
        sleep(2)
        self.click(self.filters_button)

    def select_want_to_buy_filter(self):
        sleep(2)
        checkbox = self.find_element(*self.want_to_buy_checkbox)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.want_to_buy_checkbox)
        )
        checkbox.click()

    def apply_filter(self):
        button = self.find_element(*self.apply_filter_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        self.driver.save_screenshot('before_click.png')
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.apply_filter_button)
        )
        self.driver.execute_script("arguments[0].click();", button)

    def all_deals_have_want_to_buy_tag(self):
        elements = self.find_elements(*self.deal_tags)
        return all("Want to buy" in el.text for el in elements)
