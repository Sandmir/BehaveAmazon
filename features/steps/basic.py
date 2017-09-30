from behave import *
from library.lib_selenium import *
from  selenium import webdriver
from selenium.webdriver.support.ui import Select


# driver = webdriver.Firefox()
# driver.find_elements_by_xpath()

@then("Click the search button")
def step_impl(context):
    wait_and_click(context, "//*[@value='Go']")


@given('Enter "{item}" into the search field')
def step_impl(context, item):
    wait_and_send_keys(context, 'twotabsearchtextbox', item, 'id')


@then('Count all elements in array with more then "{star}" stars')
def step_impl(context, star):
    xpath_star = "//span[@class='a-icon-alt'][starts-with(text(),%s)]" % star
    count = len(context.browser.find_elements_by_xpath(xpath_star))
    print("There are ", count, "with", star, "stars")


@step('Click on category by img: "{details}"')
def step_impl(context, details):
    current_xpath = "//img[@alt = '%s']" % details
    wait_and_click(context, current_xpath)


@when('Change quantity: "{count}"')
def step_impl(context, count):
    select = Select(context.browser.find_element_by_id("quantity"))
    select.select_by_value(count)


@step('Change delivery address: "{new_zip}"')
def step_impl(context, new_zip):
    ship_xpath = "//span[contains(text(), 'Ship to')]/..//a"
    wait_and_click(context, ship_xpath)
    wait_and_send_keys(context, 'unifiedLocationAddrInput', new_zip, 'id')
    update_button_xpath = "//input[@aria-labelledby='unifiedLocationAddrUpdate-announce']"
    wait_and_click(context, update_button_xpath)


@then('Verify "{count}" amount of items were added to the cart')
def step_impl(context, count):
    actual_count = get_text(context, 'nav-cart-count', 'id')
    print(actual_count)
    assert actual_count == count, "Fail!!!"


@step("Add items to to cart")
def step_impl(context):
    wait_and_click(context, 'add-to-cart-button', 'id')


@given('Click on any element on home page by text: "{var}"')
def step_impl(context, var):
    var_path = "//*[text()='%s']" % var
    wait_and_click(context, var_path)


@step('Click on department category: "{category}"')
def step_impl(context, category):
    category_xpath = "//a[text()='%s']" % category
    wait_and_click(context, category_xpath)


@then('Create list of all elements in carousel')
def step_impl(context):
    next_page_button = "//*[text()='Next page']/.."
    first_book_on_page = "//*[@id='anonCarousel1']//li[1]//span[@class='a-size-base']"
    first_title = get_text(context, first_book_on_page)

    list_of_books = []

    next_title = ''
    while next_title != first_title:
        wait_and_click(context, next_page_button)
        next_title = get_text(context, first_book_on_page)
        books = context.browser.find_elements_by_xpath("//*[@id='anonCarousel1']//span[@class='a-size-base']")
        for b in books:
            book_title = b.text
            list_of_books.append(book_title)

    print(list_of_books)


@step("Select the first available item")
def step_impl(context):
    first_book_on_page = "//*[@id='anonCarousel1']//li[1]//span[@class='a-size-base']"
    wait_and_click(context, first_book_on_page)


@step('Click on category by text: "{category}"')
def step_impl(context,category):
    wait_and_click(context, "//*[text()='%s']" % category)


@then("Choose format")
def step_impl(context):
    format_xpath = "a-autoid-2-announce"
    wait_and_click(context, format_xpath, 'id')


@then("Choose only new one")
def step_impl(context):
    new_checkbox = "//input[@name = 'olpCheckbox_new']"
    wait_and_click(context, new_checkbox)


@then('Choose "{quantity}"th item')
def step_impl(context, quantity):
    quantity = int(quantity) - 1
    id_xpath = 'a-autoid-%s' % quantity
    wait_and_click(context, id_xpath, 'id')

