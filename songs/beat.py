from random import random
import math
samplerate = 8000

b='20201020' # pattern

A=0
decay=0.03*(44100/samplerate)

def MAIN(t):
    global A
    n=int(b[math.floor(t/(samplerate/8))%len(b)])
    c=(n==2 and (math.floor(t%(samplerate/len(b)))==0))*255
    if n==1: A=255
    else:
        if A<=0 or not(n==0 or n==1):
            A=0
        else:
            A=A-decay
    return random()*A+c