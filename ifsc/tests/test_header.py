from ifsc.factory.browserfactory import BrowserFactory
from ifsc.pages.header import Header


def get_chrome_browser():
    browserFactory = BrowserFactory()
    chrome_driver = browserFactory.get_browser("https://www.ifsc-climbing.org/")
    return chrome_driver


def test_click_home():
    browser = None
    try:
        browser = get_chrome_browser()
        header = Header(browser)
        header = header.click_accept_all_cookies()
        header = header.click_home()
    except Exception as ex:
        assert False, "test_click_home: Exception: " + str(ex)
    finally:
        browser.close()
