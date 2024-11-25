from Sensor.exception import SensorException
import os
import sys
from Sensor.logger import logging

def test_exception():
    try:
        logging.info("There is an error in the division of numbers with zero")
        a=1/0
    except Exception as e:
        raise SensorException(e,sys)

if __name__=="__main__":
    try:
        test_exception()
        pass

    except Exception as e:
        print(e)