import os 
from selenium import webdriver

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

firstname = browser.find_element_by_css_selector('[name="firstname"]')
firstname.send_keys("Сергей")

lastname = browser.find_element_by_css_selector('[name="lastname"]')
lastname.send_keys("Васильченко")

email = browser.find_element_by_css_selector('[name="email"]')
email.send_keys("ololo@ololo.ru")


file = browser.find_element_by_id("file")
file.click()


current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
file.send_keys(file_path)

button = browser.find_element_by_tag_name("button")
button.click()