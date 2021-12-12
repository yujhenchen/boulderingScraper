from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class ChromeBrowser(object):
    def __init__(self):
        super().__init__()
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def get_browser(self):
        if self.driver is not None:
            return self.driver
        else:
            print("ChromeBrowser: get_browser: self.driver is None")
            return None
