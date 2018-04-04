from LEDCONTROLLER import LedController
import time
while True:
    try:
        LedController().downloadCourses("155.133.131.126")
    except IOError:
        print "impossible de se connecter"
    list = LedController().getCourses()
    try:
        ledlist = LedController().HandleCourses(list)
        print ledlist
        LedController().LedtoTurnOn(ledlist)
        time.sleep(1200)
        LedController().LedtoTurnOff(ledlist)
    except TypeError:
        print "fichier distant intraitable"

