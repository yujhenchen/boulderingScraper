from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Waits(object):
    wait_time = 5

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.wait = WebDriverWait(driver, self.wait_time)

    def get_presence_of_element_located(self, by):
        return self.wait.until(EC.presence_of_element_located(by))
