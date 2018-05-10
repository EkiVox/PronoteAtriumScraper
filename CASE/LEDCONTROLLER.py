#-*- coding: utf-8 -*-
import pickle
import urllib
import RPi.GPIO as GP
import requests
GP.setmode(GP.BCM)

class LedController:
    def fetchCourses(self, ip, id, day):
        response = requests.get("http://" + ip + ":8000/fetch?id=" + id + "&?day=" + day + "")
        print response
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 503:
            return "IDError"
        elif response.status_code == 404:
            return "BadID"

    def HandleCourses(self, list):
        led_to_turn = []
        courses = list[0]
        teachers = list[1]
        for cours in enumerate(courses):
            if cours[1] == "Prof. absent" or cours[1] == "Cours annul":
                del courses[cours[0]]
                del teachers[cours[0]]
            elif cours[1] == "Exceptionnel":
                courses[cours[0]] = teachers[cours[0]]
                teachers[cours[0]] = "Indeterminable"
            elif cours[1] == "Changement de salle":
                courses[cours[0]] = teachers[cours[0]]
                teachers[cours[0]] = "Indeterminable"
            elif cours[1] == u"Cours modifi":
                courses[cours[0]] = teachers[cours[0]]
                teachers[cours[0]] = "Indeterminable"
        print courses
        for cours in courses:
            if cours == "PHYS-CHIM.":
                led_to_turn.append(19)

            elif cours == "ACCOMPAGNEMT. PERSO.":
                led_to_turn.append(20)

            elif cours == "MATHEMATIQUES":
                led_to_turn.append(18)

            elif cours == "ED.PHYSIQUE & SPORT.":
                led_to_turn.append(13)

            elif cours == "ESPAGNOL LV2":
                led_to_turn.append(21)

            elif cours == "SCIENCES INGENIEUR":
                led_to_turn.append(23)

            elif cours == "FRANCAIS":
                led_to_turn.append(24)

            elif cours == "HISTOIRE & GEOGRAPH.":
                led_to_turn.append(25)

            elif cours == "ANG. LV1":
                led_to_turn.append(26)
                
        return led_to_turn

    def LedtoTurnOn(self, ledlist):
        GP.setmode(GP.BOARD)
        for i in ledlist:
            GP.setup(i,GP.OUT)
            GP.output(i,True)

    def LedtoTurnOff(self, ledlist):
        for i in ledlist:
            GP.setup(i,GP.OUT)
            GP.output(i,False)
        GP.cleanup()
    def exit(self):
        GP.cleanup()

        


"""
PHYS-CHIM.
ACCOMPAGNEMT. PERSO.
MATHEMATIQUES
ED.PHYSIQUE & SPORT.
ESPAGNOL LV2
SCIENCES INGENIEUR
FRANCAIS
HISTOIRE & GEOGRAPH.
ANG. LV1
"""
