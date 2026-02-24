import pygame
import time 
pygame.init()
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

img = pygame.image.load("image4.jpeg")
image = pygame.transform.scale(img,(WIDTH,HEIGHT))

img2 = pygame.image.load("image5.jpeg")
image2 = pygame.transform.scale(img2,(WIDTH,HEIGHT))

img3 = pygame.image.load("image6.jpeg")
image3 = pygame.transform.scale(img3,(WIDTH,HEIGHT))


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
    time.sleep(3)
    screen.blit(image2,(0,0))
    font = pygame.font.SysFont("Times New Roman", 30)
    
    text3 = font.render("You are a wonderful mom!", True, (0,0,0))
    screen.blit(text3,(30,200))

    text4 = font.render("SO grateful for you!", True, (0,0,0))
    screen.blit(text4,(30,100))
    

    pygame.display.update()
    time.sleep(5)
    screen.blit(image3,(0,0))
    font = pygame.font.SysFont("Times New Roman", 30)
    
    text5 = font.render("I love you!", True, (0,0,0))
    screen.blit(text5,(100,200))

    pygame.display.update()
    time.sleep(5)


