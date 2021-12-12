from ifsc.factory.chromebrowser import ChromeBrowser


class BrowserFactory(object):
    def __init__(self):
        super().__init__()
        self.chrome = ChromeBrowser()

    def get_browser(self, url):
        if self.chrome is not None:
            driver = self.chrome.get_browser()
            driver.get(url)
            return driver
        else:
            print("BrowserFactory: get_browser: self.chrome is None")
            return None
