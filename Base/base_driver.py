import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BaseDriver:
    def __init__(self,driver):
        self.driver=driver
        self.wait = WebDriverWait(driver, 10) 

    def page_scroll(self):
          # Scroll to the bottom of the page to load all flights
            pagelength = self.driver.execute_script("return document.body.scrollHeight;")
            match = False
            while not match:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                new_pagelength = self.driver.execute_script("return document.body.scrollHeight;")
                if new_pagelength == pagelength:
                    match = True
                else:
                    pagelength = new_pagelength
            time.sleep(4)


    def wait_for_presence_of_all_element(self,locator):
         list_of_element=self.wait.until(EC.presence_of_all_elements_located((locator)))
         return list_of_element

    def element_to_be_clickable(self,locatortype,locator):
         element=self.wait.until(EC.element_to_be_clickable((locatortype,locator)))
         return element
         

          
