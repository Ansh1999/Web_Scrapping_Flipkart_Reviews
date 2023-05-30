import os
import logging
import time as t

##if __name__=='__main__':

path = os.path.join(os.getcwd(),"LOGS")
os.makedirs(path,exist_ok=True)
filepath = os.path.join('LOGS',f"{t.asctime()}.log")
#f = open(file=filepath,mode="r")

logging.basicConfig(
        filename=filepath,
        level=logging.INFO,
        format="[%(asctime)s] - %(lineno)s - %(levelname)s - %(message)s"
        )
    
