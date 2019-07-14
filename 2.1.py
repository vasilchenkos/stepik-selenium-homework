from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

# human_radio = browser.find_element_by_id("humanRule")
# human_checked = human_radio.get_attribute("checked")
# print("value of human radio: ", human_checked)
# assert human_checked is not None, "Human radio is not selected by default"

# robots_radio = browser.find_element_by_id("robotsRule")
# robots_checked = robots_radio.get_attribute("checked")
# print("value of robot radio: ", robots_checked)
# assert robots_checked is None, "Robot radio is not selected by default"




x_element = browser.find_element_by_id("treasure")
get_int = x_element.get_attribute("valuex")
x = get_int

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


# spacestring