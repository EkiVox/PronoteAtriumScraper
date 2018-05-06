import pickle
import urllib
import RPi.GPIO as GP
import requests


class LedController:
    def fetchCourses(self, ip, id):
        response = requests.get("http" + ip + ":8000/fetch?id=" + id + "")
        if response.status_code = 200:
            return response.json()
        elif response.status_code = 503:
            return "IDError"

    def HandleCourses(self, list):
        led_to_turn = []
        courses = list[0]
        teachers = list[1]
        for cours in enumerate(courses):
            if cours[1] == "Prof. absent":
                del courses[cours[0]]
                del teachers[cours[0]]
        for cours in courses:
            if cours == "PHYS-CHIM.":
                led_to_turn.append(7)

            elif cours == "ACCOMPAGNEMT. PERSO.":
                led_to_turn.append(11)

            elif cours == "MATHEMATIQUES":
                led_to_turn.append(12)

            elif cours == "ED.PHYSIQUE & SPORT.":
                led_to_turn.append(13)

            elif cours == "ESPAGNOL LV2":
                led_to_turn.append(15)

            elif cours == "SCIENCES INGENIEUR":
                led_to_turn.append(16)

            elif cours == "FRANCAIS":
                led_to_turn.append(18)

            elif cours == "HISTOIRE & GEOGRAPH.":
                led_to_turn.append(22)

            elif cours == "ANG. LV1":
                led_to_turn.append(29)
                
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
    def exit(self)
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