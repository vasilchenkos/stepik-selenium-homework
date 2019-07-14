from selenium import webdriver
import math

browser = webdriver.Chrome()
link = "https://busfor.ru/ru/support"
browser.get(link)

name = browser.find_element_by_css_selector('[placeholder="Как вас зовут"]')
name.send_keys("Сергей")

email = browser.find_element_by_css_selector('[placeholder="ivanovpetr@mail.ru"]')
email.send_keys("ivanovpetr@mail.ru")

radio = browser.find_element_by_css_selector('[value="no"]')
radio.click()

description = browser.find_element_by_tag_name("textarea")
description.send_keys("Ситуация сложилась следующим образом ...")



checkbox = browser.find_element_by_id("checkbox")
search_checkbox = browser.find_element_by_css_selector('[for ="agreement"]')
search_checkbox.click()

button = browser.find_element_by_tag_name("button")
browser.execute_script("window.scrollBy(0, 200);")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button) //скролл отработает до конца страницы
# checkbox = browser.find_element_by_class("content__block__content-input-group")
# checkbox.click()
# button.click()
# assert True



# search_checkbox = browser.find_element_by_tag_name("checkbox")
# search_checkbox.click()

# agreement = browser.find_element_by_id("checkbox-4465420ec5cc9")
# agreement.click()

# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))

# y = calc(x)

# print('Значение переменной равно = ' + y)

# button = browser.find_element_by_tag_name("button")
# # browser.execute_script("window.scrollBy(0, 100);")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()
# assert True

# search_input = browser.find_element_by_css_selector("[id='answer']")
# search_input.send_keys(y)
# search_input.click()

# search_checkbox = browser.find_element_by_css_selector("[id='robotCheckbox']")
# search_checkbox.click()

# search_rb = browser.find_element_by_css_selector("[id='robotsRule']")
# search_rb.click()

# buttoncl = browser.find_element_by_tag_name("button")
# buttoncl.click()

# spacestring