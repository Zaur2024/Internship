
from time import sleep
from behave import given, when, then
from pages.main_page import MainPage
from pages.secondary_deals_page import SecondaryDealsPage
from pages.loginPage import loginPage
from selenium.webdriver.support import expected_conditions as EC


@given("the user opens the main page")
def step_open_main_page(context):
    context.main_page = MainPage(context.driver)
    context.main_page.open()

@given("the user is logged in")
def step_login(context):
    context.login_page = loginPage(context.driver)
    context.login_page.login("zaur.huseynov283@gmail.com", "Zxcvb12345.")

@when("the user clicks on the Secondary option")
def step_click_secondary(context):
    context.main_page.click_secondary()

@when("the user clicks on Filters")
def step_click_filters(context):
    context.secondary_page = SecondaryDealsPage(context.driver)
    context.secondary_page.click_filters()

@when('the user filters by "want to buy"')
def step_filter_want_to_buy(context):
    context.secondary_page.select_want_to_buy_filter()


@when("the user clicks Apply Filter")
def step_apply_filter(context):
    context.secondary_page.apply_filter()
    sleep(2)
    context.driver.wait.until(
        EC.presence_of_all_elements_located(context.secondary_page.deal_tags)
    )

    elements = context.secondary_page.find_elements(*context.secondary_page.deal_tags)
    print("Deal tags found after filter:")
    for el in elements:
        print(f"- {el.text}")

@then('all cards have a "Want to buy" tag')
def step_verify_tags(context):
    assert context.secondary_page.all_deals_have_want_to_buy_tag(), "Not all deals have 'Want to buy' tag"
