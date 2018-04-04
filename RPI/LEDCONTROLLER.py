import pickle
import urllib
import RPi.GPIO

class LedController:
    def downloadCourses(self, ip):
        urllib.urlretrieve ("http://" + ip + ":8000/last-courses.conf", "last-courses.conf")
    def getCourses(self):
        try:
            coursesfile = open('last-courses.conf', 'r')
            courseslist = pickle.load(coursesfile)
            return courseslist
        except (OSError, IOError, EOFError):
            print "veuillez creer un fichier last-courses.conf ou alors il est vide"
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
        GP.setmode(GP.BOARD)
        for i in ledlist:
            GP.setup(i,GP.OUT)
            GP.output(i,False)
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