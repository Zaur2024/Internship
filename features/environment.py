from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app.application import Application
from selenium.webdriver.chrome.options import Options # for headless mode


#from selenium.webdriver.firefox.service import Service
#from webdriver_manager.firefox import GeckoDriverManager


def browser_init(context):
    """
    :param context: Behave context
    """

    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no window)
    chrome_options.add_argument("--disable-gpu")  # Fix for Windows
    chrome_options.add_argument("--window-size=1920,1080")  # Set screen size for headless
    chrome_options.add_argument("--no-sandbox")  # Needed in some environments
    chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent crash in CI

    # Chrome
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service, options=chrome_options)

    # Firefox
    #driver_path = GeckoDriverManager().install()
    #service = Service(driver_path)
    #context.driver = webdriver.Firefox(service=service)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
