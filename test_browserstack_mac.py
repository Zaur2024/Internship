from selenium import webdriver
from selenium.webdriver.chrome.options import Options

caps = {
    'os': 'MAC',   # Changed from 'OS X' to 'MAC'
    'os_version': 'Monterey',
    'browserName': 'Safari',
    'browser_version': '15.6',
    'bstack:options': {
        'userName': 'zaurhuseynov_RGnVfT',
        'accessKey': 'Bpxz1kHxgyFay9guBc4K',
        'buildName': 'browserstack-build-1',
        'sessionName': 'Sample Mac Safari Test'
    }
}

options = Options()
options.set_capability('bstack:options', caps['bstack:options'])
options.set_capability('browserName', caps['browserName'])
options.set_capability('browserVersion', caps['browser_version'])
options.set_capability('platformName', caps['os'])

driver = webdriver.Remote(
    command_executor='https://hub-cloud.browserstack.com/wd/hub',
    options=options
)

driver.get("https://www.example.com")
print("Title of the page is:", driver.title)

driver.quit()
