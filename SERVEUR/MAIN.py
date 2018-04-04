import time

from FETCHER import automateFetch
import os

os.system("sh startsrv.sh")
while True:
    automateFetch().automateFetch()
    print "fetched"
    time.sleep(600)