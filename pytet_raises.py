import pytest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome()

def test_exception():
    with pytest.raises(NoSuchElementException):
    	browser.find_element_by_css_selector("button.btn")
    	pytest.fail("Не должно быть кнопки Отправить")
    # browser.get("http://selenium1py.pythonanywhere.com/")
    # with pytest.raises(NoSuchElementException, match="Не должно быть кнопки Отправить"):
    #     browser.find_element_by_css_selector("button.btn")