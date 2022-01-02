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
            self.waits.getInvisibilityOfElementLocated(locator)
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
                By,
                "div[1]/div[4]/div/div/div/div[2]/div[" + newsIndex + "]/article/h2/a",
            )
            news = self.findNews(locator)
            if news == None:
                break
            # find news link
            newsLink = news.get_attribute("href")
            newsMap[news] = newsLink
            newsIndex += 1
        return newsMap
