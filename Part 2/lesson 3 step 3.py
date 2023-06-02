from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "https://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()


def calc(x_number):
    return str(math.log(abs(12 * math.sin(int(x_number)))))


try:
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # дождаться отрисовки алерта
    WebDriverWait(browser, 5).until(EC.alert_is_present()).accept()

    y = calc(browser.find_element("id", "input_value").text)

    browser.find_element("id", "answer").send_keys(y)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(11)
    browser.quit()
