from PRONOTE import CoursesFetcher
from PRONOTE import Atrium
import time
import os
import pickle
#Main Program
os.system("clear")
CoursesFetcher().initialize()
didstorereuseoranon = raw_input("Voulez vous utiliser des anciens identifiants[1] ou vous connecter[2]?")
os.system("clear")

if didstorereuseoranon == "1": #reuse the last IDs stored
    try:
        creditentials = Atrium().reuseCreditentials()
        print "connexion..."
        CoursesFetcher().login(creditentials[0], creditentials[1])
        os.system("clear")
    except:
        print  "Impossible de se connecter"
        quit()
elif didstorereuseoranon == "2": #Connect using new IDs
    creditentials = Atrium().getCreditentials()
    os.system("clear")
    doyouwanttostore = raw_input("Voulez vous enregistrer ces identifiants[1] ou pas[2]?")
    os.system("clear")

    if doyouwanttostore == "1": #store IDs
        Atrium().storeCreditentials(creditentials)
        print "Voila voila!!!"
    elif doyouwanttostore == "2": #don't store IDs
        print "Pas d'prob chef!"
    else: #little problem... don't store the IDs
        print "Parametre invalide... \npour evitez manoeuvre non voulu, les identifiants ne s'enregistrent pas"
    print "connexion..."
    try:
        CoursesFetcher().login(creditentials[0], creditentials[1])
        os.system("clear")
    except:
        print "impossible se connecter"
        quit()


else: #Invalid input
    print "parametre invalide"
    quit()


try:
    print "fetching..."
    courseslist = CoursesFetcher().fetch() #fetch courses and teaches
    os.system("clear")
    CoursesFetcher().close() #Close browser
    print "affichage..."
    CoursesFetcher().displaying(courseslist[0], courseslist[1]) #display the returned courses and teaches
    CoursesFetcher().saveCourses(courseslist)
except:
    print "impossible de recuperer les cours"
    quit()
