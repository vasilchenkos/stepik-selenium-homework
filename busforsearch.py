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
option2.send_keys("Киев")
option2.click()
time.sleep(1)

option3 = browser.find_element_by_id("on")
option3.click()
time.sleep(1)



option4 = browser.find_element_by_css_selector("[id='passengers']")
option4.click()
time.sleep(1)


button = browser.find_element_by_css_selector('[id="submit"]')
button.click()
time.sleep(4)


# book = browser.find_elements_by_by_css_selector('[button="Выбрать"]')
# book.click()

info = browser.find_element_by_class('search__empty__title')
info2=info.text
print(info2)

# spacestring