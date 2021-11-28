from factory.waits import Waits
from factory.actions import Actions

class PageBase(object):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.waits = Waits(self.driver)
        self.actions = Actions()
