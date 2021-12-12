from ifsc.factory.waits import Waits

class PageBase(object):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.waits = Waits(self.driver)