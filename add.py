from selenium import webdriver

link = "http://suninjuly.github.io/find_xpath_form"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_elements_by_xpath('/html/body/div/form/div[6]/button[3]')

button = browser.find_element_by_css_selector("button.btn")

#пустая строка