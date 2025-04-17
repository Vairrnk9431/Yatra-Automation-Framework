import logging
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Base.base_driver import BaseDriver
from Utilities.Utils import Utils

class SearchFlightResult(BaseDriver):
    
    def __init__(self,driver):
        super().__init__(driver)
        self.log=Utils.custom_logger(loglevel=logging.WARNING)
        

        #LOCATERS
    NONE_STOP_XPATH=(By.XPATH, "//label[@class='i-b mr-5 fs-12 cursor-pointer item text-center pr '][1]")    
    ONE_STOP_XPATH=(By.XPATH, "//label[@class='i-b mr-5 fs-12 cursor-pointer item text-center pr '][2]")
    TWO_STOP_XPATH=(By.XPATH, "//label[@class='i-b mr-5 fs-12 cursor-pointer item text-center pr '][3]")
    GET_FLIGHT_SEARCH_RESULT=(By.XPATH,"//div[@class='fs-12']")

    def get_filter_flights_none_stop(self):
         return self.wait.until(EC.element_to_be_clickable(self.NONE_STOP_XPATH))

    def get_filter_flights_one_stop(self):
         return self.wait.until(EC.element_to_be_clickable(self.ONE_STOP_XPATH))

    def get_filter_flights_two_stop(self):
         return self.wait.until(EC.element_to_be_clickable(self.TWO_STOP_XPATH)) 
    
    def get_filter_search_result(self):
         return self.wait_for_presence_of_all_element(self.GET_FLIGHT_SEARCH_RESULT)
             

    def get_filter_flights_by_stops(self,by_stop):
         if by_stop == "1 stop":
              self.get_filter_flights_one_stop().click()
              self.log.warning("Selected flights with 1 stop")
              time.sleep(2)
         elif by_stop == "2 stop":
              self.get_filter_flights_two_stop().click()
              self.log.warning("Selected flights with 2 stop")
              time.sleep(2)
         elif by_stop == "0 stop":
              self.get_filter_flights_none_stop().click()
              self.log.warning("Selected flights with non stop")
              time.sleep(2) 
         else:
               self.log.warning("Please provide the valid filter option")         
      


         
              
              
       

      





        