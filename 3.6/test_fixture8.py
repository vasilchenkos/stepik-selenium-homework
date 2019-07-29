import pytest
from selenium import webdriver

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
        link = "http://selenium1py.pythonanywhere.com/{}/".format(language)
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_navbar_element(self, browser, language):
    	link = "http://selenium1py.pythonanywhere.com/{}/".format(language)
    	browser.get(link)
    	browser.find_element_by_css_selector("#login_link")