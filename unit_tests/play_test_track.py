# https://forums.raspberrypi.com/viewtopic.php?t=112006#p767726

import pygame
import time
import sounddevice as sd

devices = sd.query_devices()
print("All devices:", len(devices), devices)
for i in range(len(devices)):
    device = devices[i]
    print(f"Playing audio on device: {i}: {device}")
    sd.default.device = i

	pygame.mixer.init()
	pygame.mixer.music.load("../../Documents/test.mp3")
	pygame.mixer.music.set_volume(1.0)
	pygame.mixer.music.play()
	time.sleep(10)
	pygame.mixer.music.stop()


while pygame.mixer.music.get_busy() == True:
	pass
