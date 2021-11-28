from ifsc.factory.browserfactory import BrowserFactory

from ifsc.pages.header import Header

def get_chrome_browser():
    browserFactory = BrowserFactory()
    chrome_driver = browserFactory.get_browser("https://www.ifsc-climbing.org/")
    return chrome_driver

def test_click_home():
    header = Header(get_chrome_browser())
    header.click_home()