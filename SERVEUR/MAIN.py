import time
from threading import Thread
from FETCHER import automateFetch
import SimpleHTTPServer
import SocketServer

while True:
    automateFetch().automateFetch()
    print "fetched"
    time.sleep(600)
