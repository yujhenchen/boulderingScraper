from ifsc.factory.browserfactory import BrowserFactory
from ifsc.pages.header import Header


def get_chrome_browser():
    browserFactory = BrowserFactory()
    chrome_driver = browserFactory.get_browser("https://www.ifsc-climbing.org/")
    return chrome_driver


def test_click_accept_all_cookies():
    browser = None
    try:
        browser = get_chrome_browser()
        browser.maximize_window()

        header = Header(browser)
        header = header.click_accept_all_cookies()
        header = header.wait_cookies_dialog_close()
    except Exception as ex:
        assert False, "test_click_accept_all_cookies: Exception: " + str(ex)
    finally:
        browser.close()
