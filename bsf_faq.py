from selenium import webdriver
import math

browser = webdriver.Chrome()
link = "https://busfor.ru/ru/faq"
browser.get(link)

name = browser.find_element_by_css_selector('[placeholder="Поиск темы или вопроса"]')
name.send_keys("билет")



button = browser.find_element_by_class("body > div:nth-child(3) > div.container.faq-header > div > a > div")
browser.execute_script("window.scrollBy(0, 200);")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button) //скролл отработает до конца страницы
checkbox.click()
button.click()
assert True
