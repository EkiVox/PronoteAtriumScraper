import alsaaudio as audio

some_value = 2000

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


