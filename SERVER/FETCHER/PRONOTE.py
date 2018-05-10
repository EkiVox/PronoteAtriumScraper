# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC 
import os
import getpass
import pickle
import time





#Getting Atrium creditentials in terminal class
class Atrium:
    def storeCreditentials(self,id, credits):
        try:
            with open('user/' + id + '/creditentials-' + id + '.conf', 'w') as creditsfile:
                pickle.dump(credits, creditsfile)
        except (OSError, IOError, EOFError):
            print "veuillez creer un fichier creditentials.conf"

    def reuseCreditentials(self, id):
        try:
            creditsfile = open('user/' + id + '/creditentials-' + id + '.conf', 'r')
            credits = pickle.load(creditsfile)
            return credits
        except (OSError, IOError, EOFError):
            return "BadID"
    def getCreditentials(self):
        USERNAME = raw_input('Username: ')
        PASSWORD = getpass.getpass('Password (no echoing): ')
        return [USERNAME, PASSWORD]


#initialize browser, connect to atrium and fetch courses class
class CoursesFetcher:
    def initialize(self): #initialise the chrome browser
        global browser
        global options
        #setup headless
        options = webdriver.ChromeOptions()
        #options.add_argument('headless')
        #setup chromedriver
        browser = webdriver.Chrome(chrome_options=options)
        browser.implicitly_wait(15)

    def login(self, identifiant, motdepasse): #Login chrome to atrium and redirect to pronote
        browser.get("https://www.atrium-paca.fr/connexion/login?service=https:%2F%2F0831563Y.index-education.net%2Fpronote%2Fmobile.eleve.html%3Fredirect=1")
        browser.find_element_by_id("username").clear()
        browser.find_element_by_id("username").send_keys(identifiant)
        browser.find_element_by_id("password").clear()
        browser.find_element_by_id("password").send_keys(motdepasse)
        browser.find_element_by_name("submit").click()

    def fetch(self,day): #fetch next courses and teachers using pronote
        try:
            time.sleep(5)
            assert u"LPO COSTEBELLE - PRONOTE - Espace Élèves" in browser.title
            browser.find_element_by_xpath("(//a[contains(text(),'Tout voir')])[2]").click()
            day = int(day)
            if day < 0:
                day = -1*day
                for x in range(day):
                    if x == 0:
                        time.sleep(0.5)
                    time.sleep(0.5)
                    browser.find_element_by_id("GInterface.Instances[1].Instances[0]_JourPrecedent").click()
                    if x == day-1:
                        time.sleep(1.5)

            elif day > 0:
                for x in range(day):
                    if x == 0:
                        time.sleep(0.5)
                    time.sleep(0.5)
                    browser.find_element_by_id("GInterface.Instances[1].Instances[0]_JourSuivant").click()
                    if x == day-1:
                            time.sleep(1.5)

            coursinit = browser.find_elements_by_xpath("//*[@id='GInterface.Instances[1].Instances[2]']/ul/li/div/div[1]") #fetch courses
            cours = [x.text.encode('ascii','ignore') for x in coursinit] #take the name of courses and put into a dictionnary

            profsinit = browser.find_elements_by_xpath("//*[@id='GInterface.Instances[1].Instances[2]']/ul/li/div/div[2]") #fetch teachers
            profs = [x.text.encode('ascii','ignore') for x in profsinit] #take the name of teachers and put into a dictionnary
            return cours, profs #return a dictionnary with courses and teachers
        except Exception:
            return "ConnectionError"
            
    def displaying(self, cours, profs): #display the courses and teachers in a table
        os.system('clear')
        print '#####################################'
        print '#          COURS : PROFS            #'
        print '#####################################\n'
        for cours, profs in zip(cours, profs):
            print(cours + " : " + profs + '\n')
        print '#####################################\n'
        raw_input()

    def saveCourses(self, courseslist, id): #save courses to last-courses.conf
        try:
            with open('user/' + id + '/last-courses-' + id + '.conf', 'w') as coursesfile:
                pickle.dump(courseslist, coursesfile)
        except (OSError, IOError, EOFError):
            print "veuillez creer un fichier last-courses.conf"

    def close(self): #close the browser for avoid chrome to run in background
        browser.quit()


#Xpathdevoircontenu = //*[@id="GInterface.Instances[1].Instances[0]_DetailleTaf_4F3CBA297D4E"]/div[1]/text()
#Xpath day courses = //*[@id="GInterface.Instances[1].Instances[0]_JourCourant"]/text()
#nextday course = browse.find_element_by_id("GInterface.Instances[1].Instances[0]_JourSuivant").click()

