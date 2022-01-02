from ifsc.pages.home import Home
import traceback


def testFetchOnePageNews():
    home = None
    try:
        home = Home()
        home.clickAcceptAllCookies()
        home.waitCookiesDialogClose()
        news = home.clickNews()

        news.clickAcceptAllCookies()
        news.waitCookiesDialogClose()
        newsMap = news.fetchOnePageNews()

        # print(len(newsMap))
        for key in newsMap:
            print(key + "  " + newsMap[key])
    except Exception as ex:
        traceback.print_exc()
        assert False, "testFetchOnePageNews"
    finally:
        home.driver.close()
        news.driver.close()
