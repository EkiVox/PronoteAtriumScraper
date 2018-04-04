from threading import Thread
import time
from FETCHER import automateFetch
from LEDCONTROLLER import LedController

class FetchandHandle(Thread):

    def __init__(self):
        Thread.__init__(self)

    def Fetch(self):
        while True:
            automateFetch().automateFetch()
            time.sleep(600)
            
    def Handle(self):
        while True:
            LedController().getCourses()
            time.sleep(1200)

# Creation des threads
thread_1 = FetchandHandle().Fetch()
thread_2 = FetchandHandle().Handle()

# Lancement des threads
thread_1.start()
thread_2.start()

