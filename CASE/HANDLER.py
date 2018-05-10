#-*- coding: utf-8 -*-
from LEDCONTROLLER import LedController
import time

i = 0
ledlist = ""
oldangle = 0
angle = 0

def handling(i):
    try:
        if ledlist != "":
            LedController().LedtoTurnOff(ledlist)
        with open('courses/day' + i + '/courses.list', 'r') as coursesfile:
            list  = pickle.load(coursesfile)
        ledlist = LedController().HandleCourses(list)
        print ledlist
        LedController().LedtoTurnOn(ledlist)
    except:
        print "Erreur lors du processus" 
        ledlist = ""
        LedController().exit()
        time.sleep(1)
    
@skywriter.flick()
def flick(start,finish):
    print('Got a flick!', start, finish)
    if start = "east" and finish = "west":
        i = i+1
        handling(i)
        print "handling" + str(i)
    elif start = "west" and finish = "east":
        i = i-1
        handling(i)
        print "handling" + str(i)

def spinny(delta):
    angle += delta
    print angle
    if angle < 0:
        angle = 0
    if 340 <= angle - oldangle <= 380:
        handling(i)
        print "handling" + str(i)
        angle = 0
        oldangle = angle