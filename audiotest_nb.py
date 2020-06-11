import pyaudio
import time
import numpy as np

CHANNELS = 1
RATE = 44100
freq = 220
CHUNK = 1024
lastchunk = 0
DAUER=1.5 #Sekunden
VOL=0.2

#def sine(current_time):
def sine():
    global freq,lastchunk
    length = CHUNK
    factor = float(freq)*2*np.pi/RATE
    this_chunk = np.arange(length)+lastchunk
    lastchunk = this_chunk[-1]
    return np.sin(this_chunk*factor)

def get_chunk(): 
#    data  = sine(time.time())
    data  = sine()
    return data * VOL


def callback(in_data, frame_count, time_info, status):
    chunk = get_chunk() * 0.25
    data = chunk.astype(np.float32).tostring()
    return (data, pyaudio.paContinue)

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paFloat32,
            channels=CHANNELS,
            rate=RATE,
            frames_per_buffer=CHUNK,
            output=True,
            stream_callback=callback)

stream.start_stream()

akt_time=time.time()

while stream.is_active() and (akt_time+DAUER)>time.time():
    time.sleep(0.1)   

stream.stop_stream()

freq=440
stream.start_stream()
akt_time=time.time()

while stream.is_active() and (akt_time+DAUER)>time.time():
    time.sleep(0.1)   

stream.stop_stream()

freq=880
stream.start_stream()
akt_time=time.time()

while stream.is_active() and (akt_time+DAUER)>time.time():
    time.sleep(0.1)   

stream.stop_stream()


stream.close()

