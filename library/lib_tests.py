from library.lib_selenium import wait_and_click


def delete_items_from_cart(driver):
    wait_and_click(driver, 'nav-cart', 'id')
    wait_and_click(driver, "//input[@value='Delete']")
    driver.browser.get('https://www.amazon.com/')