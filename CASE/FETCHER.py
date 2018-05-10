import pickle
import time
import os
from LEDCONTROLLER import LedController

while True:
    for i in range(-10, 11):
        try:
            idfile = open("identifiant.conf", "r")
            id = idfile.read().replace("\n","")
            idfile.close()
            list = LedController().fetchCourses("sccase.tk", id, i)
            if list == "IDError":
                print "Erreur d'acces au serveur ou d'identifiant"
            elif list == "BadID":
                print "Mauvais ID"
            else:
                os.makedirs('courses/day' + i + '/')
                with open('courses/day' + i + '/courses.list', 'w') as coursesfile:
                    pickle.dump(list, coursesfile)
        except:
            print "Erreur lors du processus" 
            time.sleep(1)
    time.sleep(600)
