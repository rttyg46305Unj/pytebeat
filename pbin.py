from random import random

samplerate = 44100

def MAIN(t):
    global r
    if t%(samplerate/4)==0:
        r=random()*8
    return t*r