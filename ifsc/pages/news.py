from ifsc.pages.pagebase import PageBase


class News(PageBase):
    def __init__(self):
        super().__init__()
        self.url = "https://www.ifsc-climbing.org/index.php/news"
        self.driver.get(self.url)
        self.driver.maximize_window()
