#-*- coding: utf-8 -*-
from LEDCONTROLLER import LedController
import time
import alsaaudio as audio
import signal
import pickle
import os
import skywriter

menu = "led"
some_value = 7000
i = 0
ledlist = ""
allled = [13, 18, 19, 20, 21, 23, 24, 25, 26]
isplaying = False

def handling(i):
    try:
        global ledlist
        if ledlist != "":
            LedController().LedtoTurnOff(ledlist)
        with open('courses/day' + str(i) + '/courses.list', 'r') as coursesfile:
            list  = pickle.load(coursesfile)
        ledlist = LedController().HandleCourses(list)
        print ledlist
        LedController().LedtoTurnOn(ledlist)
    except Exception as e:
        print "Erreur lors du processus" 
        ledlist = ""
        print e
        LedController().exit()
        time.sleep(1)

@skywriter.flick()
def flick(start,finish):
    global i
    global menu
    global allled
    global isplaying

    print('Got a flick!', start, finish)
    if start == "east" and finish == "west":
        if menu == "led":
            i = i-1
            if i == -11:
                i = -10
            handling(i)
            print "handling " + str(i)
        elif menu == "music":
            os.system("mpc prev")

    elif start == "west" and finish == "east":
        if menu == "led":
            i = i+1
            if i == 11:
                i = 10
            handling(i)
            print "handling " + str(i)
        elif menu == "music":
            os.system("mpc next")

    elif start == "south" and finish == "north":
        if menu == "led":
            i = 0
            handling(i)
            print "handling " + str(i)
        elif menu == "music":
            menu = "led"
            handling(i)
            print "handling " + str(i)

    elif start == "north" and finish == "south":
        if menu == "led":
            menu = "music"
            for i in allled:
                LedController().LedtoTurnOn([i])
                time.sleep(0.2)
        elif menu == "music":
            if isplaying == False
                os.system("mpc play")
                isplaying = True
            elif isplaying == True:
                os.system("mpc pause")
                isplaying = False


mixer = audio.Mixer('PCM', cardindex=0)

@skywriter.airwheel()
def spinny(delta):
    global ledlist
    global some_value
    some_value += delta
    if some_value < 0:
        some_value = 0
    if some_value > 8000:
        some_value = 8000
    print('Airwheel:', some_value/80)
    if menu == "music":
        print mixer.getvolume()
        mixer.setvolume(int(some_value/80))
        LedController().LedtoTurnOn([13, 18, 19, 20, 21, 23, 24, 25, 26], int(some_value/80))
    elif menu == "led":
        LedController().LedtoTurnOn(ledlist, int(some_value/80))

mixer.setvolume(87)
handling(0)

signal.pause()
#def spinny(delta):
#    angle += delta
#    print angle
#    if angle < 0:
#        angle = 0
#    if 340 <= angle - oldangle <= 380:
#        handling(i)
#        print "handling" + str(i)
#        angle = 0
#        oldangle = angle
