
import logging
import time
from selenium.webdriver.common.by import By
from Base.base_driver import BaseDriver
from Pages.search_result_page import SearchFlightResult
from Utilities.Utils import Utils


class Launchpage(BaseDriver):
    
    def __init__(self,driver):
        super().__init__(driver)
        self.log=Utils.custom_logger(loglevel=logging.WARNING)
        

    #LOCATERS
    DEPART_FROM_FIELD="//div[@aria-label='Departure From New Delhi inputbox']"
    DEPART_FROM_INPUTFIELD="//input[@id='input-with-icon-adornment']"
    DEPART_FROM_LOCATION_SELECT="//div[contains(text(), 'Kolkata, (CCU)')]"
    GOING_TO_FIELD="//div[@aria-label='Going To Mumbai inputbox']"
    GOING_TO_INPUTFIELD="//input[@id='input-with-icon-adornment']"
    GOING_TO_LOCATION_SELECT="//div[contains(text(), 'Bangalore, (BLR)')]"
    DATE_PICKER_FIELD="//div[@class='css-w7k25o']"
    DATE_PICKER="//div[@aria-label='Choose Saturday, May 31st, 2025']"


    #departure field
    def departfield(self):
        return self.element_to_be_clickable(By.XPATH, self.DEPART_FROM_FIELD).click()

    def departInput(self,location):
        self.log.warning("clicked on departure field")
        input_field = self.element_to_be_clickable(By.XPATH, self.DEPART_FROM_INPUTFIELD)
        input_field.click()
        input_field.send_keys(location)
        
    def set_departure(self):
        self.element_to_be_clickable(By.XPATH, self.DEPART_FROM_LOCATION_SELECT).click()


    #going to field
    def goingTofield(self):
        return self.element_to_be_clickable(By.XPATH, self.GOING_TO_FIELD).click()

    def goingToInput(self,location):
        self.log.warning("clicked on goingto field")
        input_field = self.element_to_be_clickable(By.XPATH, self.GOING_TO_INPUTFIELD)
        input_field.click()
        input_field.send_keys(location)
        
    def set_goingTo(self):
        self.element_to_be_clickable(By.XPATH, self.GOING_TO_LOCATION_SELECT).click()


    def open_date_picker(self):
        self.element_to_be_clickable(By.XPATH, self.DATE_PICKER_FIELD).click()

    def select_date(self):
        self.element_to_be_clickable(By.XPATH, self.DATE_PICKER).click()
        self.log.warning("date is selected")


    def searchbtn(self):
        self.element_to_be_clickable(By.XPATH, "//button[@type='button']").click()
        time.sleep(4)

        

    def searchflight(self,departurelocattion,goingtoloaction):
        self.departfield()
        self.departInput(departurelocattion)
        self.set_departure()
        self.goingTofield()
        self.goingToInput(goingtoloaction)
        self.set_goingTo()
        self.open_date_picker()
        self.select_date()
        self.searchbtn()
        search_result = SearchFlightResult(self.driver)
        return search_result




       