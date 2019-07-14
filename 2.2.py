from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

x = browser.find_element_by_css_selector("[id='num1']")
x_get = x.text
y = browser.find_element_by_css_selector("[id='num2']")
y_get = y.text

def sum(x,y):
	return str(int(x_get) + int(y_get))

z = sum(x,y)
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(z) 

button = browser.find_element_by_css_selector("button.btn")
button.click()