#-*- coding: utf-8 -*-
from LEDCONTROLLER import LedController
import time
import alsaaudio as audio
import signal

some_value = 2000
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
    global i
    print('Got a flick!', start, finish)
    if start == "east" and finish == "west":
        i = i+1
        handling(i)
        print "handling " + str(i)
    elif start == "west" and finish == "east":
        i = i-1
        handling(i)
        print "handling " + str(i)
    elif start == "south" and finish == "north":
        i = 0
        handling(i)
        print "handling " + str(i)



mixer = audio.Mixer('PCM', cardindex=0)
@skywriter.airwheel()
def spinny(delta):
    global some_value
    some_value += delta
    if some_value < 0:
        some_value = 0
    if some_value > 4000:
        some_value = 4000
    print('Airwheel:', some_value/40)
    print mixer.getvolume()
    mixer.setvolume(int(some_value/40))

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