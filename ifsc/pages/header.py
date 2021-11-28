from pagebase import PageBase
from selenium.webdriver.common.by import By


class Header(PageBase):
    home_by = (By.CSS_SELECTOR, "a[href*='/index.php']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_home(self):
        return
