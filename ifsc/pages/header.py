from ifsc.pages.pagebase import PageBase
from selenium.webdriver.common.by import By


class Header(PageBase):
    home_by = (By.CSS_SELECTOR, "a[href*='/index.php']")
    accept_all_cookies_by = (By.ID, "onetrust-accept-btn-handler")

    def __init__(self, driver):
        super().__init__(driver)

    def click_home(self):
        home_link = self.waits.get_presence_of_element_located(self.home_by)
        home_link.click()
        return self

    def click_accept_all_cookies(self):
        accept_button = self.waits.get_presence_of_element_located(
            self.accept_all_cookies_by
        )
        accept_button.click()
        return self
