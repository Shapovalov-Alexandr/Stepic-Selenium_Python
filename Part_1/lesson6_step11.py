from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()

try:
    browser.get(link1)

    # Ваш код, который заполняет обязательные поля
    firstName = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    firstName.send_keys("John")
    lastName = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    lastName.send_keys("Doe")
    eMail = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    eMail.send_keys("jd@gmail.com")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

try:
    browser.get(link2)

    # Ваш код, который заполняет обязательные поля
    firstName = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    firstName.send_keys("John")
    lastName = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    lastName.send_keys("Doe")
    eMail = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    eMail.send_keys("jd@gmail.com")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
