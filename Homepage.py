""""python selenium automation using action chains to drag and drop
DATE : 21-12-2024
NAME : SUJATHA
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from time import sleep

class Data:
    URL = "https://jqueryui.com/droppable/"

class Locators:
    SOURCE = "draggable"
    TARGET = "droppable"
    iframe_element = "iframe.demo-frame"

class DragAndDropUsingActionChains(Data, Locators):
    def __init__(self):

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.actions = ActionChains(self.driver)

    def drag_drop(self):
        try:

            self.driver.maximize_window()
            self.driver.get(self.URL)
            sleep(2)

            # Switch to the iframe
            iframe = self.driver.find_element(by=By.CSS_SELECTOR, value=self.iframe_element)
            self.driver.switch_to.frame(iframe)
            sleep(2)  # Wait  iframe is fully loaded


            source = self.driver.find_element(by=By.ID, value=self.SOURCE)
            target = self.driver.find_element(by=By.ID, value=self.TARGET)


            self.actions.drag_and_drop(source, target).perform()


            sleep(3)

        except (NoSuchElementException, ElementNotVisibleException) as error:

            print(f"Error occurred: {error}")

        finally:

            self.driver.quit()



if __name__ == "__main__":
    sujatha = DragAndDropUsingActionChains()
    sujatha.drag_drop()



