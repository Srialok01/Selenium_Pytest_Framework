
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait


class HomePage():
    def __init__(self, driver):
        self.driver = driver

        self.Electronics_xpath = "//ul[@class='top-menu notmobile']//a[contains(text(),'Electronics ')]"
        self.Cell_Phones_xpath = "//ul[@class='top-menu notmobile']//a[contains(text(),'Cell phones')]"
        self.Others_xpath = "//ul[@class='top-menu notmobile']//a[contains(text(),'Others')]"

    def Hover(self):
        hoverElement = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(self.Electronics_xpath))
        hover = ActionChains(self.driver)
        hover.move_to_element(hoverElement).perform()

    def NavigateToCellPhone(self):
        self.Hover()
        element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(self.Cell_Phones_xpath))
        element.click()
        time.sleep(2)

    def NavigateToOthers(self):
        self.Hover()
        element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(self.Others_xpath))
        element.click()
        time.sleep(2)
