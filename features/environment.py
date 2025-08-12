from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from pages.secondary_deals_page import SecondaryDealsPage

def browser_init(context):
    caps = {
        'os': 'MAC',
        'osVersion': 'Monterey',
        'browserName': 'Safari',
        'browserVersion': '15.6',
        'bstack:options': {
            'userName': 'zaurhuseynov_RGnVfT',
            'accessKey': 'Bpxz1kHxgyFay9guBc4K',
            'buildName': 'My Build',
            'sessionName': context.scenario.name if hasattr(context, 'scenario') else 'Test Session',
            'local': False
        }
    }

    options = Options()
    options.set_capability('bstack:options', caps['bstack:options'])
    options.set_capability('browserName', caps['browserName'])
    options.set_capability('browserVersion', caps['browserVersion'])
    options.set_capability('platformName', caps['os'])

    context.driver = webdriver.Remote(
        command_executor='https://hub-cloud.browserstack.com/wd/hub',
        options=options
    )

    context.driver.implicitly_wait(10)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.driver.maximize_window()

def before_scenario(context, scenario):
    print(f"\nStarting scenario: {scenario.name}")
    context.scenario = scenario
    browser_init(context)
    context.secondary_page = SecondaryDealsPage(context.driver)

def after_scenario(context, scenario):
    context.driver.quit()
    print(f"\nFinished scenario: {scenario.name}")
