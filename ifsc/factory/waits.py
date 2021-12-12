from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Waits(object):
    wait_time = 10

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.wait = WebDriverWait(driver, self.wait_time)

    def get_presence_of_element_located(self, by):
        return self.wait.until(EC.presence_of_element_located(by))

    def get_element_to_be_clickable(self, by):
        return self.wait.until(EC.element_to_be_clickable(by))

    def get_invisibility_of_element_located(self, by):
        return self.wait.until(EC.invisibility_of_element_located(by))
