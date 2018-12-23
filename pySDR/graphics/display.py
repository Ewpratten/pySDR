import pygame
import pygame.freetype
from scipy.interpolate import interp1d


m = interp1d([0,10], [0,400])
m2 = None

pygame.init()

black = (0,0,0)
white = (255,255,255)
grey = (100,100,100)
red = (200,0,0)
green = (0,200,0)
blue = (0,0,200)
amber = (255, 239, 213)


gameDisplay = pygame.display.set_mode((1024,400))
pygame.display.set_caption('pySDR')
gameDisplay.fill(white)
pygame.display.update()

def clear():
	global gameDisplay
	gameDisplay.fill(white)
	pygame.display.update()

def plot(x,y):
	global gameDisplay
	m2(x)
	gameDisplay.set_at((int(round(float(m2(x)))), int(round(float(m(y))))), black)
	print([int(round(float(m2(x)))), int(round(float(m(y)))),m(y)])
	pygame.display.update()
	
def setParams(freq):
	global m2
	freq = freq / 1000000
	print(freq)
	m2 = interp1d([freq - 2, freq + 2], [0,1024])