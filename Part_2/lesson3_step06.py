from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()


def calc(x_number):
    return str(math.log(abs(12 * math.sin(int(x_number)))))


try:
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "button.trollface").click()

    # переключение на новое окно браузера
    browser.switch_to.window(browser.window_handles[1])

    y = calc(browser.find_element("id", "input_value").text)

    browser.find_element("id", "answer").send_keys(y)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(11)
    browser.quit()
