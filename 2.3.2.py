from selenium import webdriver
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

button = browser.find_element_by_css_selector("button.trollface")
button.click()

# browser.switch_to.window(window_name)
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

# option1 = browser.find_element_by_tag_name("button")
# option1.click()

# confirm = browser.switch_to.alert
# confirm.accept()

x_element = browser.find_element_by_css_selector("[id='input_value']")
x = x_element.text

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

input = browser.find_element_by_css_selector("[id='answer']")
input.send_keys(y)

button = browser.find_element_by_css_selector("button.btn")
button.click()

