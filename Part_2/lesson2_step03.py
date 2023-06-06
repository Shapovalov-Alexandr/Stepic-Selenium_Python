from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
# import math

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()


def find_sum(x, y):
    return str(x + y)


try:
    browser.get(link)

    x_el = int(browser.find_element(By.ID, "num1").text)
    y_el = int(browser.find_element(By.ID, "num2").text)

    answer_sum = find_sum(x_el, y_el)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(answer_sum)

    btn = browser.find_element(By.CSS_SELECTOR, "button.btn-default")
    btn.click()

finally:
    time.sleep(11)
    browser.quit()
