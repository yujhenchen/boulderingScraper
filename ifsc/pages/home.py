from ifsc.pages.pagebase import PageBase
from selenium.webdriver.common.by import By
from ifsc.pages.news import News


class Home(PageBase):
    home_by = (By.XPATH, "//nav/div[2]/ul/li[1]/a")
    news_by = (By.XPATH, "//nav/div[2]/ul/li[6]/a")
    dialog_div = (By.ID, "onetrust-banner-sdk")
    accept_all_cookies_by = (
        By.XPATH,
        "/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div/button[3]",
    )

    def __init__(self):
        super().__init__()
        self.url = "https://www.ifsc-climbing.org/index.php"
        self.driver.get(self.url)
        self.driver.maximize_window()

    def clickHome(self):
        home_link = self.waits.waitForElementToBeClickable(self.home_by)
        home_link.click()
        return self

    def clickNews(self):
        news_link = self.waits.waitForElementToBeClickable(self.news_by)
        news_link.click()
        news = News()
        return news

    def clickAcceptAllCookies(self):
        accept_button = self.waits.waitForElementToBeClickable(
            self.accept_all_cookies_by
        )
        accept_button.click()
        return self

    def waitCookiesDialogClose(self):
        dialog_div = self.waits.getInvisibilityOfElementLocated(self.dialog_div)
        return self
