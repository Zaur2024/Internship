from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from pages.secondary_deals_page import SecondaryDealsPage

def browser_init(context):
    mobile_emulation = {"deviceName": "Nexus 5"}
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")

    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=chrome_options)
    context.driver.implicitly_wait(10)
    context.driver.wait = WebDriverWait(context.driver, 10)

def before_scenario(context, scenario):
    print(f"\nStarting scenario: {scenario.name}")
    context.scenario = scenario
    browser_init(context)
    context.secondary_page = SecondaryDealsPage(context.driver)

def after_scenario(context, scenario):
    context.driver.quit()
    print(f"\nFinished scenario: {scenario.name}")
