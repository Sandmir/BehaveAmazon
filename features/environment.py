from selenium import webdriver


from library.lib_tests import delete_items_from_cart


def before_all(context):

    context.browser = webdriver.Firefox(executable_path='/Applications/Python 3.5/geckodriver')
    context.browser.implicitly_wait(10)

    context.browser.maximize_window()
    context.browser.get('https://www.amazon.com/')

def after_all(context):
    context.browser.quit()
    # pass

def  before_scenario(context, scenario):
    context.browser.get('https://www.amazon.com/')


def  after_scenario(context, scenario):
    delete_items_from_cart(context)
    # pass
