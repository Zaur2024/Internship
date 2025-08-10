
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app.application import Application
from pages.secondary_deals_page import SecondaryDealsPage

""" Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
"""
# Firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def browser_init(context):
    """
    :param context: Behave context
    """

    #chrome_options = Options()
    #chrome_options.add_argument("--headless")
    #chrome_options.add_argument("--disable-gpu")
    #chrome_options.add_argument("--window-size=1920,1080")

    #chrome_options.add_argument("--no-sandbox")
    #chrome_options.add_argument("--disable-dev-shm-usage")
    #chrome_options.add_argument("--disable-extensions")
    #chrome_options.add_argument("--disable-infobars")

    #driver_path = ChromeDriverManager().install()
    #service = Service(driver_path)
    #context.driver = webdriver.Chrome(service=service, options=chrome_options)



    #context.driver.maximize_window()

# ---------------- Firefox setup (uncomment to use Firefox) ----------------
    firefox_options = FirefoxOptions()
    firefox_options.headless = False  # Change to True for headless mode
    firefox_options.add_argument("--width=1920")
    firefox_options.add_argument("--height=1080")

    driver_path = GeckoDriverManager().install()
    service = FirefoxService(driver_path)
    context.driver = webdriver.Firefox(service=service, options=firefox_options)
    context.driver.implicitly_wait(10)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)
    context.driver.maximize_window()


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)
    context.secondary_page = SecondaryDealsPage(context.driver)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
