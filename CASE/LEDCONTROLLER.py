#-*- coding: utf-8 -*-
import pickle
import urllib
import RPi.GPIO as GP
import requests

allledlist = [13, 18, 19, 20, 21, 23, 24, 25, 26]
def initializer():
    global allledlist
    GP.setmode(GP.BCM)
    for i in allledlist:
        GP.setup(i,GP.OUT)
        globals()["p" + str(i)] = GP.PWM(i, 1000)
        globals()["p" + str(i)].start(0)

class LedController:
    def fetchCourses(self, ip, id):
        response = requests.get("https://" + ip + ":21/fetchall?id=" + id + "")
        print response
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 503:
            return "IDError"
        elif response.status_code == 404:
            return "BadID"

    def HandleCourses(self, list, day):
        led_to_turn = []
        courses = list[0][day]
        teachers = list[1][day]
        for cours in enumerate(courses):
            if cours[1].isupper() == False:
                courses[cours[0]] = teachers[cours[0]]
                teachers[cours[0]] = "Indeterminable"
        #print courses
        for cours in courses:
            if cours == "PHYS-CHIM.":
                led_to_turn.append(19)

            elif cours == "ACCOMPAGNEMT. PERSO.":
                led_to_turn.append(20)

            elif cours == "MATHEMATIQUES":
                led_to_turn.append(18)

            #elif cours == "ED.PHYSIQUE & SPORT.":
            #    led_to_turn.append(13)

            elif cours == "PHILOSOPHIE":
                led_to_turn.append(13)
            elif cours == "ESPAGNOL LV2":
                led_to_turn.append(21)

            elif cours == "SCIENCES INGENIEUR":
                led_to_turn.append(23)

            #elif cours == "FRANCAIS":
            #    led_to_turn.append(24)

            elif cours == "SPE MATHS":
                 led_to_turn.append(24)

            elif cours == "HISTOIRE & GEOGRAPH.":
                led_to_turn.append(25)

            elif cours == "ANG. LV1":
                led_to_turn.append(26)
            else:
                print "cours non reconnu ou n'a pas de led a son nom:" + cours
        return led_to_turn

    def LedtoTurnOn(self, ledlist, dim):
        for i in ledlist:
            try:
                globals()["p" + str(i)].ChangeDutyCycle(dim)
            except:
                globals()["p" + str(i)].ChangeDutyCycle(100)

    def LedtoTurnOff(self, ledlist):
        for i in ledlist:
            globals()["p" + str(i)].ChangeDutyCycle(0)

    def exit(self):
        GP.cleanup()
    def BCM(self):
        GP.setmode(GP.BCM)
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
SPE MATHS
PHILOSOPHIE
"""
