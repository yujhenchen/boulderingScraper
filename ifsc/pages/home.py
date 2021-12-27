from pagebase import PageBase
from selenium.webdriver.common.by import By


class Home(PageBase):
    home_by = (By.CSS_SELECTOR, "a[href*='/index.php']")
    dialog_div = (By.ID, "onetrust-banner-sdk")
    accept_all_cookies_by = (By.ID, "onetrust-accept-btn-handler")

    def __init__(self, driver):
        super().__init__(driver)

    def click_home(self):
        home_link = self.waits.waitForElementToBeClickable(self.home_by)
        home_link.click()
        return self

    def click_accept_all_cookies(self):
        accept_button = self.waits.waitForElementToBeClickable(
            self.accept_all_cookies_by
        )
        accept_button.click()
        return self

    def wait_cookies_dialog_close(self):
        dialog_div = self.waits.get_invisibility_of_element_located(self.dialog_div)
        return self
