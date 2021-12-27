from ifsc.pages.home import Home


def testAcceptAllCookies():
    home = None
    try:
        home = Home()
        home = home.clickAcceptAllCookies()
        home = home.waitCookiesDialogClose()
    except Exception as ex:
        assert False, "testAcceptAllCookies: Exception: " + str(ex)
    finally:
        home.driver.close()


def testGoToNews():
    home = None
    try:
        home = Home()
        home = home.clickAcceptAllCookies()
        home = home.waitCookiesDialogClose()
        news = home.clickNews()
    except Exception as ex:
        assert False, "testGoToNews: Exception: " + str(ex)
    finally:
        home.driver.close()
