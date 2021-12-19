from ifsc.utils.waits import Waits

from ifsc.factory.browserfactory import BrowserFactory


class PageBase(object):
    def __init__(self):
        super().__init__()
        bf = BrowserFactory()
        self.driver = bf.get_browser()
        self.waits = Waits(self.driver)