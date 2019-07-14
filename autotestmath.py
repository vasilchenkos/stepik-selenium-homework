from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_css_selector("[id='input_value']")
x = x_element.text

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

print('Значение переменной равно = ' + y)

option0 = browser.find_element_by_css_selector("[id='answer']")
option0.send_keys(y)
option0.click()

option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
option1.click()

option2 = browser.find_element_by_css_selector("[id='robotsRule']")
option2.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()


# human_radio = browser.find_element_by_id("humanRule")
# #Найдём атрибут "checked" с помощью встроенного метода get_attribute и проверим его значение:

# human_checked = human_radio.get_attribute("checked")
# print("value of human radio: ", human_checked)
# # assert human_checked is not None, "Human radio is not selected by default"
# assert human_checked == "true", "Human radio is not selected by default"

# robots_radio = browser.find_element_by_id("humanRule")
# robots_checked = robots_radio.get_attribute("checked")
# assert robots_checked is None