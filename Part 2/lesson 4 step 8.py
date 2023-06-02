from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "https://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()


def calc(x_number):
    return str(math.log(abs(12 * math.sin(int(x_number)))))


try:
    browser.get(link)

    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    browser.find_element(By.ID, "book").click()

    y = calc(browser.find_element("id", "input_value").text)

    browser.find_element("id", "answer").send_keys(y)

    browser.find_element("id", "solve").click()

finally:
    time.sleep(11)
    browser.quit()
