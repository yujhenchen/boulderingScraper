from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Waits(object):

    def __init__(self, driver, wait_time = 10):
        super().__init__()
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_time)

    def waitForElement(self, by):
        return self.wait.until(EC.presence_of_element_located(by))

    def waitForElementToBeClickable(self, by):
        return self.wait.until(EC.element_to_be_clickable(by))

    def getInvisibilityOfElementLocated(self, by):
        return self.wait.until(EC.invisibility_of_element_located(by))
