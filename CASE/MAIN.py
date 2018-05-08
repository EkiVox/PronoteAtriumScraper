#-*- coding: utf-8 -*-
from LEDCONTROLLER import LedController
import time
ledlist = ""
while True:
    try:
        idfile = open("identifiant.conf", "r")
        id = idfile.read().replace("\n","")
        idfile.close()
        list = LedController().fetchCourses("sccase.tk", id)
        if list == "IDError":
            print "Erreur d'acces au serveur ou d'identifiant"
        elif list == "BadID":
            print "Mauvais ID"
        else:
            if ledlist == "":
                print ""
            else:
                LedController().LedtoTurnOff(ledlist)
            ledlist = LedController().HandleCourses(list)
            print ledlist
            LedController().LedtoTurnOn(ledlist)
            time.sleep(600)
    except Exception as e:
        print "Erreur lors du processus" 
        print e
        LedController().exit()
