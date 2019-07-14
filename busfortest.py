from selenium import webdriver
import time

link = "https://busfor.ru/"
browser = webdriver.Chrome()
browser.get(link)

option1 = browser.find_element_by_css_selector("[id='from']")
option1.send_keys("Москва")
option1.click()
time.sleep(1)

option2 = browser.find_element_by_css_selector("[id='to']")
option2.send_keys("Воронеж")
option2.click()
time.sleep(1)

option3 = browser.find_element_by_id("on")
option3.click()
time.sleep(1)

option3 = browser.find_element_by_id("submit")
option3.click()
# Ваш код, который заполняет обязательные поля
#name = browser.find_element_by_css_selector('#submit')
#name.send_keys("Мое имя")

# first_name = browser.find_element_by_css_selector('.first_block .second')
# first_name.send_keys("Моя фамилия")

# email = browser.find_element_by_css_selector('.first_block .third')
# email.send_keys("Моя почта")


# # Отправляем заполненную форму
#button = browser.find_element_by_css_selector("button.btn")
#button.click()

# # Проверяем, что смогли зарегистрироваться
# # ждем загрузки страницы
# time.sleep(1)

# # находим элемент, содержащий текст
# welcome_text_elt = browser.find_element_by_tag_name("h1")
# # записываем в переменную welcome_text текст из элемента welcome_text_elt
# welcome_text = welcome_text_elt.text

# # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
# assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text