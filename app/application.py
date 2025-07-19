from pages.base_page import BasePage
from pages.loginPage import loginPage
from pages.main_page import MainPage
from pages.secondary_deals_page import SecondaryDealsPage

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.base_page=BasePage(driver)
        self.login_page = loginPage(driver)
        self.main_page = MainPage(driver)
        self.secondary_page = SecondaryDealsPage(driver)




