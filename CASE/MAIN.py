from LEDCONTROLLER import LedController
import time
while True:
    
    list = LedController().fetchCourses("155.133.131.126")
    if list == "IDError":
        print "Erreur d'acces au serveur ou d'identifiant"
    else:
        try:
            LedController().LedtoTurnOff(ledlist)
            ledlist = LedController().HandleCourses(list)
            print ledlist
            LedController().LedtoTurnOn(ledlist)
            time.sleep(600)
        except:
            print "erreur"
            LedController().exit()
