import pygame
import os
pygame.init()
screen = pygame.display.set_mode((600,600))
screen.fill("navy")
pygame.display.update()

inheritancegames = pygame.image.load(os.path.join("pictures","inheritancegames.jpg"))
onceuponabrokenheart = pygame.image.load(os.path.join("pictures","brokenheart.jpg"))
powerless = pygame.image.load(os.path.join("pictures","powerless.jpg"))
agoodgirlsguidetomurder = pygame.image.load(os.path.join("pictures","aggtm.jpg"))

screen.blit(inheritancegames,(150,50))

screen.blit(onceuponabrokenheart,(150,150))

screen.blit(powerless,(150,250))

screen.blit(agoodgirlsguidetomurder,(150,350))


font = (pygame.font.SysFont("comic sans", 20))

text1 = font.render("holly jackson", True,(0,0,0))
screen.blit(text1,(340,70))

text2 = font.render("jennifer lynn barnes", True,(0,0,0))
screen.blit(text2,(340,170))

text3 = font.render("stephanie garber", True,(0,0,0))
screen.blit(text3,(340,270))

text4 = font.render("lauren roberts", True,(0,0,0))
screen.blit(text4,(340,370))



while True:
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen,(0,0,0),pos,10,0)
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONUP:
            pos2 = pygame.mouse.get_pos()
            pygame.draw.circle(screen,(0,0,0),pos2,10,0)
            pygame.draw.line(screen,(0,0,0),pos,pos2,5)
            pygame.display.update()





