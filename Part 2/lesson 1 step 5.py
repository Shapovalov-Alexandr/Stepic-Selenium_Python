from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()


def calc(x_number):
    return str(math.log(abs(12 * math.sin(int(x_number)))))


try:
    browser.get(link)

    x_elem = browser.find_element(By.ID, "input_value")
    x = x_elem.text
    y = calc(x)

    answer = browser.find_element("id", "answer")
    answer.send_keys(y)

    check = browser.find_element("id", "robotCheckbox")
    check.click()

    radio = browser.find_element("id", "robotsRule")
    radio.click()

    btn = browser.find_element(By.CSS_SELECTOR, "button.btn-default")
    btn.click()

finally:
    time.sleep(10)
    browser.quit()
