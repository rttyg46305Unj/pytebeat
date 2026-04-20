# Sample binary data
import pbin, wave
from os import remove

try:
    length=pbin.lensec*pbin.samplerate
except:
    try:
        length=pbin.lensamp
    except:
        length=10**6

out=bytearray()

for t in range(0,length):
    try:
        out.append(round(pbin.MAIN(t))%256)
    except ZeroDivisionError:
        out.append(0)
# Open a file in binary write mode
with open('data.raw', 'wb') as file:
    file.write(out)
    
with open("data.raw", "rb") as inp_f:
    data = inp_f.read()
    with wave.open("sound.wav", "wb") as out_f:
        out_f.setnchannels(1)
        out_f.setsampwidth(1)
        out_f.setframerate(pbin.samplerate)
        out_f.writeframesraw(data)
        
remove('data.raw')