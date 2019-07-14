from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")



button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR")
    )
button = browser.find_element_by_css_selector("button.btn")
button.click()

x_element = browser.find_element_by_css_selector("[id='input_value']")
x = x_element.text

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

print('Значение переменной равно = ' + y)

option0 = browser.find_element_by_css_selector("[id='answer']")
option0.send_keys(y)
option0.click()

button = browser.find_element_by_css_selector("[id='solve']")
button.click()

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# button = WebDriverWait(browser, 5).until(
#         EC.element_to_be_clickable((By.ID, "check"))
#     )
# button.click()
# print("Кнопка стала активной и мы ее нажали")
# message = browser.find_element_by_id("check_message")

# assert "успешно" in message.text

# # говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
# button = WebDriverWait(browser, 5).until_not(
#         EC.element_to_be_clickable((By.ID, "check"))
#     )
# print("После нажатия кнопка стала неактивной")
# print("Тест пройден успешно")