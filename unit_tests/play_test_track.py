# https://forums.raspberrypi.com/viewtopic.php?t=112006#p767726

import pygame

pygame.mixer.init()
pygame.mixer.music.load("../../Documents/test.mp3")
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play()


while pygame.mixer.music.get_busy() == True:
	pass
