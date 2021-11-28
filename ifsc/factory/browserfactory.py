from chromebrowser import ChromeBrowser


class BrowserFactory(object):
    def __init__(self):
        super().__init__()
        self.chrome = ChromeBrowser()

    def get_browser(self):
        if self.chrome is not None:
            return self.chrome.get_browser()
        else:
            print("BrowserFactory: get_browser: self.chrome is None")
            return None
