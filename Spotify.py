# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time

is_playing = False
is_random = False




user = "Username or email here"
passwd = "password here"









class Spotify:
    def initialize(self): #initialise the chrome browser
        global browser
        global options
        #setup headless
        options = webdriver.ChromeOptions()
        #options.add_argument('headless')
        #setup chromedriver
        browser = webdriver.Chrome(executable_path='./chromedriver',chrome_options=options)
        browser.implicitly_wait(15)

    def connect(self, USERNAME, PASSWORD):
        browser.get("https://open.spotify.com/browse")
        browser.find_element_by_id("has-account").click()
        browser.find_element_by_id("login-username").clear()
        browser.find_element_by_id("login-username").send_keys(USERNAME)
        browser.find_element_by_id("login-password").clear()
        browser.find_element_by_id("login-password").send_keys(PASSWORD)
        browser.find_element_by_id("login-password").click()
        browser.find_element_by_id("g-recaptcha-button").click()

    def PlayLastPlayed(self):
        browser.find_element_by_xpath("//div[@id='main']/div/div[2]/div/nav/div/div/ul/div/li/a/span").click()
        time.sleep(5)
        browser.find_element_by_xpath("//div[@id='main']/div/div[2]/div[2]/div/div/section/div/div/div/header/div[2]/button").click()
        is_playing = True
    
    def play_or_pause(self):
        browser.find_element_by_xpath("//div[@id='main']/div/div[3]/footer/div/div[2]/div/div/button[3]").click()


    def close(self): #close the browser for avoid chrome to run in background
        browser.quit()

#browser.find_element_by_xpath("//div[@id='main']/div/div[3]/footer/div/div[2]/div/div/button[3]").click()
#browser.find_element_by_xpath("//div[@id='main']/div/div[3]/footer/div/div[2]/div/div/button[4]").click()
#browser.find_element_by_xpath("//div[@id='main']/div/div[3]/footer/div/div[2]/div/div/button[2]").click()
#browser.find_element_by_xpath("//div[@id='main']/div/div[3]/footer/div/div[2]/div/div/button").click()


Spotify().initialize() #initialize browser
Spotify().connect(user, passwd) #connect to spotify
try:
    Spotify().PlayLastPlayed() #lance le derniere album/son/musique ecoute
    raw_input() #laisse tourner pour pouvoir gerer avec telephone jusqu'a qu'on appuie sur entree
    Spotify().close() #ferme spotify
except NoSuchElementException as e:
    Spotify().close()
