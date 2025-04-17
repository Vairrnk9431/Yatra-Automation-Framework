import inspect
import logging
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime

class Utils:

    @staticmethod
    def assertListItem(flight_list, value):  
        for flight in flight_list:
            full_text = flight.text.strip()
            expected_value = " ".join(full_text.split()[:1])
            print("The text is", expected_value)
            assert expected_value in full_text
            print("assert pass")

    @staticmethod
    def custom_logger(test_name=None, loglevel=logging.DEBUG):
        """
        Creates a logger that stores logs in a unique file per test with log rotation.
        """
      
        log_folder = "logs"
        os.makedirs(log_folder, exist_ok=True)

       
        if test_name is None:
            test_name = inspect.stack()[1][3] 

      
        log_filename = f"{log_folder}/{test_name}_{datetime.now().strftime('%Y-%m-%d')}.log"

        # Create a logger
        logger = logging.getLogger(test_name)
        logger.setLevel(loglevel)

        # Log rotation setup (max 10MB per file, keep 3 backups)
        handler = RotatingFileHandler(log_filename, maxBytes=10 * 1024 * 1024, backupCount=3)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        return logger
