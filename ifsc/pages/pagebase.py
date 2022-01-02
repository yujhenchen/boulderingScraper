from ifsc.utils.waits import Waits
from selenium.webdriver.common.by import By
from ifsc.factory.browserfactory import BrowserFactory


class PageBase(object):
    dialog_div = (By.ID, "onetrust-banner-sdk")
    accept_all_cookies_by = (
        By.XPATH,
        "/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div/button[3]",
    )

    def __init__(self):
        super().__init__()
        bf = BrowserFactory()
        self.driver = bf.get_browser()
        self.waits = Waits(self.driver)

    def clickAcceptAllCookies(self):
        accept_button = self.waits.waitForElementToBeClickable(
            self.accept_all_cookies_by
        )
        accept_button.click()
        return self

    def waitCookiesDialogClose(self):
        dialog_div = self.waits.getInvisibilityOfElementLocated(self.dialog_div)
        return self
