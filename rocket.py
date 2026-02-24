import pygame
from time import *

pygame.init()
screen = pygame.display.set_mode((500,500))
playerx = 100
playery = 10

player = pygame.image.load("spaceship.png")

background = pygame.image.load("space_background.png")
background = pygame.transform.scale(background,(500,500))

keys = [False, False, False, False]

while playery < 450:
    screen.blit(background,(0,0))
    screen.blit(player,(playerx,playery))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
        if event.type == pygame.KEYDOWN:         #keypressed
            if event.key == pygame.K_UP:
                keys[0] = True
            if event.key == pygame.K_LEFT:
                keys[1] = True
            if event.key == pygame.K_DOWN:
                keys[2] = True
            if event.key == pygame.K_RIGHT:
                keys[3] = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys[0] = False
            if event.key == pygame.K_LEFT:
                keys[1] = False
            if event.key == pygame.K_DOWN:
                keys[2] = False
            if event.key == pygame.K_RIGHT:
                keys[3] = False

    if keys[0]:
        if playery > 0:
            playery -= 7
    if keys[1]:
        if playerx > 0:
            playerx -= 7
    if keys[2]:
        if playery < 450:
            playery += 7
    if keys[3]:
        if playerx < 450:
            playerx += 7

    playery += 5
    sleep(0.05)

print("GAME OVER! Try again!") 
       
        




