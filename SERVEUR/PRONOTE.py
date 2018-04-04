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
    def storeCreditentials(self, credits):
        try:
            creditsfile = open('creditentials.conf', 'w')
            pickle.dump(credits, creditsfile)
        except (OSError, IOError, EOFError):
            print "veuillez creer un fichier creditentials.conf"
    def reuseCreditentials(self):
        try:
            creditsfile = open('creditentials.conf', 'r')
            credits = pickle.load(creditsfile)
            return credits
        except (OSError, IOError, EOFError):
            print "veuillez creer un fichier creditentials.conf ou alors il est vide"
        
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
        options.add_argument('headless')
        #setup chromedriver
        browser = webdriver.Chrome(executable_path='../chromedriver',chrome_options=options)
        browser.implicitly_wait(15)

    def login(self, identifiant, motdepasse): #Login chrome to atrium and redirect to pronote
        browser.get("https://www.atrium-paca.fr/connexion/login?service=https:%2F%2F0831563Y.index-education.net%2Fpronote%2Fmobile.eleve.html%3Fredirect=1")
        browser.find_element_by_id("username").clear()
        browser.find_element_by_id("username").send_keys(identifiant)
        browser.find_element_by_id("password").clear()
        browser.find_element_by_id("password").send_keys(motdepasse)
        browser.find_element_by_name("submit").click()

    def fetch(self): #fetch next courses and teachers using pronote
        try:
            time.sleep(5)
            assert u"LPO COSTEBELLE - PRONOTE - Espace Élèves" in browser.title
            browser.find_element_by_xpath("(//a[contains(text(),'Tout voir')])[2]").click()

            coursinit = browser.find_elements_by_xpath("//*[@id='GInterface.Instances[1].Instances[2]']/ul/li/div/div[1]") #fetch courses
            cours = [x.text.encode('ascii','ignore') for x in coursinit] #take the name of courses and put into a dictionnary

            profsinit = browser.find_elements_by_xpath("//*[@id='GInterface.Instances[1].Instances[2]']/ul/li/div/div[2]") #fetch teachers
            profs = [x.text.encode('ascii','ignore') for x in profsinit] #take the name of teachers and put into a dictionnary
            return cours, profs #return a dictionnary with courses and teachers
        except Exception:
            print "Erreur de connexion ou d'identification"
            
    def displaying(self, cours, profs): #display the courses and teachers in a table
        os.system('clear')
        print '#####################################'
        print '#          COURS : PROFS            #'
        print '#####################################\n'
        for cours, profs in zip(cours, profs):
            print(cours + " : " + profs + '\n')
        print '#####################################\n'
        raw_input()

    def saveCourses(self, courseslist): #save courses to last-courses.conf
        try:
            coursesfile = open('last-courses.conf', 'w')
            pickle.dump(courseslist, coursesfile)
        except (OSError, IOError, EOFError):
            print "veuillez creer un fichier last-courses.conf"

    def close(self): #close the browser for avoid chrome to run in background
        browser.quit()


