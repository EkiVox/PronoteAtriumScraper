import pickle
import time
import os
import shutil
from LEDCONTROLLER import LedController

while True:
    for i in range(-10, 11):
        try:
            idfile = open("identifiant.conf", "r")
            id = idfile.read().replace("\n","")
            idfile.close()
            print "day " + str(i)
            clist = LedController().fetchCourses("sccase.tk", id, str(i))
            if clist == "IDError":
                print "Erreur d'acces au serveur ou d'identifiant"
            elif clist == "BadID":
                print "Mauvais ID"
            elif type(clist) == list or type(clist) == tuple:
                try:
                    shutil.rmtree('courses/day' + str(i) + '/')
                except:
                    print ""
                os.makedirs('courses/day' + str(i) + '/')
                with open('courses/day' + str(i) + '/courses.list', 'w') as coursesfile:
                    pickle.dump(clist, coursesfile)
                print "Courses stored"
                print "\n\n\n"
                time.sleep(5)
            else:
                "Erreur lors du processus, la reponse fourni par le serveur est intraitable"
        except Exception as e:
            print "Erreur lors du processus"
            print e 
            time.sleep(1)
    time.sleep(600)
