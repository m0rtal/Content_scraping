from tbselenium.tbdriver import TorBrowserDriver


class TorBrowser:
    def __init__(self):
        self.driver = TorBrowserDriver("C:\Tor Browser")
        # self.driver.set_window_position(-2000, 0)

    def load_page(self, url):
        self.driver.get(url)

    def find_elements_by_xpath(self, xpath):
        return self.driver.find_elements_by_xpath(xpath)

    def close(self):
        self.driver.close()
        self.driver.quit()
        print(1)
