# Sample binary data
import wave
from os import remove
from sys import argv
from math import floor
from time import sleep
import pygame.mixer as mixer

st=60

try:
    flags=argv[2:len(argv)]
except:
    flags=[]

z=0

def inside(f):
    return(f'-{f}' in flags)

try:
    song=argv[1]
except:
    print('No song given. Using pbin.')
    song='pbin'

# sssdfgf funny code
#   str(f'{var} = 1')
#   exec(a)

a = str(f'import songs.{song} as pbin')


exec(a)

try:
    length=pbin.lensec*pbin.samplerate
except:
    try:
        length=pbin.lensamp
    except:
        if inside('a'):
            length=st*pbin.samplerate
        else:
            length=10**6

try:
    rdepth=pbin.bitdepth
except:
    rdepth=1

while z==0 or inside('a'):
    depth=rdepth

    out=bytearray()

    for t in range(0,length):
        addout = floor(pbin.MAIN((z*st*pbin.samplerate)+t))%(2**(depth*8))
        if depth==0:    
            out.append(addout<<7)
        else:
            out.append(addout)

    if depth<=0:    
            depth=1

    # Open a file in binary write mode
    with open('data.raw', 'wb') as file:
        file.write(out)
        
    with open("data.raw", "rb") as inp_f:
        data = inp_f.read()
        with wave.open(f"{song}.wav", "wb") as out_f:
            out_f.setnchannels(1)
            out_f.setsampwidth(depth)
            out_f.setframerate(pbin.samplerate)
            out_f.writeframesraw(data)
            
    remove('data.raw')
    if inside('a'):
        if z==0:
            mixer.init()
        s=mixer.Sound(f"{song}.wav")
        s.play()
        try:
            sleep(st)
        except:
            remove(f"{song}.wav")
            exit()
    z+=1
print(f'Done! Saved as {song}.wav.')

