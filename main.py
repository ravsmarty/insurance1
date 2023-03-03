from Insurance.logger import logging
from Insurance.exception import InsuranceException
import sys,os


def test_logger_exception():
     try:
          logging.info("starting the test logger ad rxception")
          result = 3/0
          print(result)
          logging.info("ending point of logger_exception")
     except Exception as e:
          logging.debug(str(e))
          raise InsuranceException(e, sys)

if __name__ =="__main__":
     try:
          test_logger_exception()
     except Exception as e:
          print(e)
          #raise InsuranceException(e, sys)