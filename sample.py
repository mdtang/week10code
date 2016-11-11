#How to draw shapes

#required 
import pygame
pygame.init();

#create colors
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (150, 0, 255)

#create a surface
gameDisplay = pygame.display.set_mode((800,600)) #initialize with a tuple

#lets add a title, aka "caption"
pygame.display.set_caption("Mingda's drawing")

pygame.display.update()		#only updates portion specified

gameExit = False
while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True

	gameDisplay.fill(purple)

	pygame.draw.rect(gameDisplay, white, [300,300, 10, 100])	
	pygame.draw.rect(gameDisplay, white, [500,300, 10, 100])
	pygame.draw.rect(gameDisplay, white, [300,100, 10, 100])
	pygame.draw.rect(gameDisplay, white, [500,100, 10, 100])
	pygame.draw.rect(gameDisplay, white, [300,500, 10, 100])
	pygame.draw.rect(gameDisplay, white, [500,500, 10, 100])
	pygame.draw.rect(gameDisplay, white, [400,500, 5, 100])
	pygame.draw.rect(gameDisplay, white, [400,200, 5, 100])

	pygame.display.update()		

#required
pygame.quit()
quit()				#exits python

