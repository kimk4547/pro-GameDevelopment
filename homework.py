import pygame
import time 
pygame.init()
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

img = pygame.image.load("image4.jpeg")
image = pygame.transform.scale(img,(WIDTH,HEIGHT))


while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((0,0,128))
    screen.blit(image,(0,0))
    font = pygame.font.SysFont("Times New Roman", 72)
    
    text1 = font.render("Happy", True, (0,0,0))
    screen.blit(text1,(210,180))

    text2 = font.render("Mother's Day!", True, (0,0,0))
    screen.blit(text2, (160,264))
    

    pygame.display.update()
    time.sleep(5)
