import pickle
import time
import os
import shutil
from LEDCONTROLLER import LedController
from time import strftime

while True:
    try:
        idfile = open("identifiant.conf", "r")
        id = idfile.read().replace("\n","")
        idfile.close()
        print "[" + strftime(%Y-%m-%d %H:%M:%S, datetime.now()) + "] Fetching all courses"
        clist = LedController().fetchCourses("sccase.tk", id)
        if clist == "IDError":
            print "Erreur d'acces au serveur ou d'identifiant"
        elif clist == "BadID":
            print "Mauvais ID"
        elif type(clist) == list or type(clist) == tuple:
            try:
                shutil.rmtree('courses/')
            except:
                print ""
            os.makedirs('courses/')
            with open('courses/courses.list', 'w') as coursesfile:
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
