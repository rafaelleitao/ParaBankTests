from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.common.by import By

def is_element_present(driver, how, what):
    try:
        driver.find_element(by=how, value=what)
    except NoSuchElementException:
        return False
    return True

def is_alert_present(driver):
    try:
        driver.switch_to.alert
    except NoAlertPresentException:
        return False
    return True

def close_alert_and_get_its_text(driver):
    try:
        alert = driver.switch_to.alert
        alert_text = alert.text
        if driver.accept_next_alert:
            alert.accept()
        else:
            alert.dismiss()
        return alert_text
    finally:
        driver.accept_next_alert = True