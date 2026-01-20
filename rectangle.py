import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

screen.fill("pink")

class Rectangle():
    def __init__(self, color, dimension):
        self.color = color
        self.dimension = dimension
        self.rect_surface = screen

    def drawRectangle(self):
        self.rect_draw = pygame.draw.rect(self.rect_surface, self.color, self.dimension)

#creating objects for rectangle class:
navyBlueRect = Rectangle("#0c0b47",(50,20,100,120)) #<--- x, y, width, height
navyBlueRect.drawRectangle()

darkRedRect = Rectangle("#521413", (20,30,50,60))
darkRedRect.drawRectangle()

sageGreenRect = Rectangle("#677849", (100,40,49,82))
sageGreenRect.drawRectangle()

pinkRect = Rectangle("#de97b6", (300,400,65,345))
pinkRect.drawRectangle()



while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    
