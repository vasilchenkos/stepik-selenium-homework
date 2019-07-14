from selenium import webdriver
import time

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/cats.html")

button = browser.find_element_by_id("button")

# button = browser.find_element_by_id("check")
# button.click()
# message = browser.find_element_by_id("check_message")

# assert "Проверка прошла успешно!" in message.text
# print("test passed")
# if browser.find_element_by_id("check_message").text == 'Проверка прошла успешно!':
# 	browser.close()