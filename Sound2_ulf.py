# Sound2a.py

from soundplayer import SoundPlayer
import time

# Sine tone during 0.1 s, blocking, device 0
dev = 0
print ("Blocking Soundausgabe")
print ("Sound1")
SoundPlayer.playTone(900, 1, True, dev) # 900 Hz
print ("Sound2")
SoundPlayer.playTone(800, 0.5, True, dev) # 800 Hz
print ("Sound3")
SoundPlayer.playTone(600, 1, True, dev) # 600 Hz
#time.sleep(1)
print ("Sound4")
#SoundPlayer.playTone([900, 800, 600], 2, True, dev) # 3 tones together
SoundPlayer.playTone(10000, 3, True, dev) # 3 tones together
print ("done")

#print("Nonblocking Soundausgabe")
#print ("Sound1")
#SoundPlayer.playTone(900, 3, False, dev) # 900 Hz
#print ("Sound2")
#SoundPlayer.playTone(800, 3, False, dev) # 800 Hz
#print ("Sound3")
#SoundPlayer.playTone(600, 3, False, dev) # 600 Hz
#time.sleep(1)
#print ("done")
