import pytest
from selenium import webdriver
import time
import math

answer = math.log(int(time.time()))


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('language', ["ru", "en-gb"])
class TestLogin(object):
    def test_guest_should_see_login_link(self, browser, language):
        link = "https://stepik.org/lesson/236895/step/1".format(language)
        browser.get(link)
        

    def test_guest_should_see_navbar_element(self, browser, language):
    	link = "https://stepik.org/lesson/236896/step/1".format(language)
    	browser.get(link)
    	