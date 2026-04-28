import pygame
import random
import time

pygame.init()
pygame.display.set_caption("Have a Healthy Body!")

screen_width = 900
screen_height = 700

screen = pygame.display.set_mode([screen_width,screen_height])

def change_background(image):
    bg = pygame.image.load(image)
    bg = pygame.transform.scale(bg,(900,700))
    screen.blit(bg,(0,0))


class Bodybuilder(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("bodybuilder.png")

        self.image = pygame.transform.scale(self.image,(40,60))

        self.rect = self.image.get_rect()