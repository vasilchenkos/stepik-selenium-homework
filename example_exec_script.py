from selenium import webdriver
import math

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

x_element = browser.find_element_by_css_selector("[id='input_value']")
x = x_element.text

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

print('Значение переменной равно = ' + y)

button = browser.find_element_by_tag_name("button")
# browser.execute_script("window.scrollBy(0, 100);")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
assert True

search_input = browser.find_element_by_css_selector("[id='answer']")
search_input.send_keys(y)
search_input.click()

search_checkbox = browser.find_element_by_css_selector("[id='robotCheckbox']")
search_checkbox.click()

search_rb = browser.find_element_by_css_selector("[id='robotsRule']")
search_rb.click()

buttoncl = browser.find_element_by_tag_name("button")
buttoncl.click()
