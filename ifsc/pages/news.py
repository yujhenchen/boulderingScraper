from ifsc.pages.pagebase import PageBase
from selenium.webdriver.common.by import By


class News(PageBase):
    dialog_div = (By.ID, "onetrust-banner-sdk")
    accept_all_cookies_by = (
        By.XPATH,
        "/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div/button[3]",
    )

    def __init__(self):
        super().__init__()
        self.url = "https://www.ifsc-climbing.org/index.php/news"
        self.driver.get(self.url)
        self.driver.maximize_window()

    def findNews(self, locator):
        try:
            return self.waits.waitForElementToBeClickable(locator)
        except:
            return None

    def fetchOnePageNews(self):
        newsMap = {}
        # newsTitle = (By, "/html/body/div[1]/div[4]/div/div/div/div[2]/div[1]/article/h2/a")
        # "/html/body/div[1]/div[4]/div/div/div/div[2]/div[2]/article/h2/a"

        newsIndex = 1
        while True:
            # find news
            locator = (
                By.XPATH,
                "//div[1]/div[4]/div/div/div/div[2]/div["
                + str(newsIndex)
                + "]/article/h2/a",
            )
            news = self.findNews(locator)
            if news == None:
                break
            # find news link
            newsLink = news.get_attribute("href")
            newsMap[news.text] = newsLink
            newsIndex += 1
        return newsMap

    def clickAcceptAllCookies(self):
        accept_button = self.waits.waitForElementToBeClickable(
            self.accept_all_cookies_by
        )
        accept_button.click()
        return self

    def waitCookiesDialogClose(self):
        dialog_div = self.waits.getInvisibilityOfElementLocated(self.dialog_div)
        return self
