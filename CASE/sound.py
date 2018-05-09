#!/usr/bin/env python

import signal
import time
import skywriter
import alsaaudio as audio

some_value = 2000

#@skywriter.flick()
#def flick(start,finish):
#    print('Got a flick!', start, finish)
mixer = audio.Mixer('Headphone', cardindex=1)
#mixer = audio.Mixer()
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

#@skywriter.double_tap()
#def doubletap(position):
#    print('Double tap!', position)

#@skywriter.tap()
#def tap(position):
#    print('Tap!', position)

#@skywriter.touch()
#def touch(position):
#    print('Touch!', position)
print "launched"
signal.pause()
