from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
# print(os.path.abspath(__file__))
# print(os.path.abspath(os.path.dirname(__file__)))

link = "https://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    browser.find_element(By.NAME, 'firstname').send_keys("Ivan")
    browser.find_element(By.NAME, 'lastname').send_keys("Petrov")
    browser.find_element(By.NAME, 'email').send_keys("111@222.333")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    browser.find_element(By.NAME, 'file').send_keys(file_path)

    browser.find_element(By.CSS_SELECTOR, "button.btn")

finally:
    time.sleep(11)
    browser.quit()
