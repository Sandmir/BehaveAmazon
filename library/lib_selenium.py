
from behave import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep

wait_time = 20


def wait_and_send_keys(driver, locator, send_text, locator_type='xpath'):
    wait = WebDriverWait(driver.browser, wait_time)
    if locator_type == 'id':
        wait.until(expected_conditions.visibility_of_element_located((By.ID, locator))).send_keys(send_text)
    elif locator_type == 'xpath':
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, locator))).send_keys(send_text)


def wait_and_click(driver, locator, locator_type='xpath'):
    wait = WebDriverWait(driver.browser, wait_time)
    if locator_type == 'id':
        wait.until(expected_conditions.element_to_be_clickable((By.ID, locator))).click()
    elif locator_type == 'xpath':
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, locator))).click()

def get_text(driver, locator, locator_type='xpath'):
    wait = WebDriverWait(driver.browser, wait_time)
    if locator_type == 'id':
        return wait.until(expected_conditions.visibility_of_element_located((By.ID, locator))).text
    elif locator_type == 'xpath':
        return wait.until(expected_conditions.visibility_of_element_located((By.XPATH, locator))).text