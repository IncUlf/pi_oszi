import pyaudio
import time
import numpy as np

CHANNELS = 1
RATE = 44100
freq = 600
CHUNK = 1024
lastchunk = 0
def sine(current_time):
    global freq,lastchunk
    length = CHUNK
    factor = float(freq)*2*np.pi/RATE
    this_chunk = np.arange(length)+lastchunk
    lastchunk = this_chunk[-1]
    return np.sin(this_chunk*factor)

def get_chunk(): 
    data  = sine(time.time())
    return data * 0.1


def callback(in_data, frame_count, time_info, status):
    chunk = get_chunk() * 0.25
    data = chunk.astype(np.float32).tostring()
    return (data, pyaudio.paContinue)

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paFloat32,
            channels=CHANNELS,
            rate=RATE,
            output=True,
            stream_callback=callback)

stream.start_stream()
time.sleep(1)   

stream.stop_stream()
stream.close()

