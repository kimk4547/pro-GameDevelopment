import pygame
import random
import time

pygame.init()
pygame.display.set_caption("Recycle Marathon!")

screen_width = 900
screen_height = 700

screen = pygame.display.set_mode([screen_width, screen_height])

def change_background(image):
    bg = pygame.image.load(image)
    bg = pygame.transform.scale(bg,(900,700))
    screen.blit(bg, (0,0))


class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("bin.png")

        self.image = pygame.transform.scale(self.image,(40,60))

        self.rect = self.image.get_rect()


class Non_Recyclable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("plastic.png")

        self.image = pygame.transform.scale(self.image,(40,40))

        self.rect = self.image.get_rect()


class Recyclable(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = pygame.image.load(image)

        self.image = pygame.transform.scale(self.image,(30,30))

        self.rect = self.image.get_rect()


item_list = pygame.sprite.Group()

plastic_list = pygame.sprite.Group()

allsprites = pygame.sprite.Group()

bin = Bin()

allsprites.add(bin)

for i in range(20):
    plastic = Non_Recyclable()

    plastic.rect.x = random.randrange(screen_width)

    plastic.rect.y = random.randrange(screen_height)

    plastic_list.add(plastic)

    allsprites.add(plastic)

    
    

