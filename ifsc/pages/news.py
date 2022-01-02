from ifsc.pages.pagebase import PageBase
from selenium.webdriver.common.by import By


class News(PageBase):
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
