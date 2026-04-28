# Sample binary data


import wave, math
from os import remove
from sys import argv
try:
    song=argv[1]
except:
    print('No song given. Using default of pbin.')
    song='pbin'

# a simple workaround, like
#   str(f'{var} = 1')
#   exec(a)

a = str(f'import songs.{song} as pbin')

try:
    exec(a)
except:
    print(f'Song {song} not found.{" Make the pbin.py file in the songs folder." if song=="pbin" else ''}')

try:
    length=pbin.lensec*pbin.samplerate
except:
    try:
        length=pbin.lensamp
    except:
        length=10**6

try:
    depth=pbin.bitdepth
except:
    depth=1

if depth<=0:
    depth=0.125
    
out=bytearray()

for t in range(0,length):
    addout = round(pbin.MAIN(t))%(2**(depth*8))
    if depth==0.125:    
        out.append(addout<<7)
    else:
        out.append(addout)

if depth==0.125:    
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
print(f'Done! Saved as {song}.wav.')