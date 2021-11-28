from ifsc.factory.browserfactory import BrowserFactory

from pages.header import Header

def get_chrome_browser():
    chrome_driver = BrowserFactory.get_browser("https://www.ifsc-climbing.org/")
    return chrome_driver

def test_click_home():
    header = Header(get_chrome_browser())
    header.click_home()