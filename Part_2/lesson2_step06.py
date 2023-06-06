from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()


def calc(x_number):
    return str(math.log(abs(12 * math.sin(int(x_number)))))


try:
    browser.get(link)

    y = calc(browser.find_element("id", "input_value").text)

    browser.find_element("id", "answer").send_keys(y)

    radio = browser.find_element("id", "robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()

    browser.find_element("id", "robotsRule").click()

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(30)
    browser.quit()
