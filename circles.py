import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)
yellow = (255,0,0)

screen.fill("pink")

position = (300,300)
radius = 50
width = 2

pygame.draw.circle(screen, red, position, radius, width)


class Mycircle:
    def __init__(self, color, position, radius, width):
        self.color = color
        self.position = position
        self.radius = radius
        self.width = width
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.position, self.radius, self.width)
    def grow(self, r):
        self.radius = self.radius + r
        pygame.draw.circle(self.screen, self.color, self.position, self.radius, self.width)
#creating objects
blue_circle = Mycircle(blue,position,radius+90,4)
green_circle = Mycircle(green,position,radius+100,5)
red_circle = Mycircle(red,position,radius+110,6)
black_circle = Mycircle(black,position,radius+120,7)
white_circle = Mycircle(white,position,radius+130,8)
yellow_circle = Mycircle(yellow,position,radius+140,9)


#inifnite loop
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            blue_circle.draw()
            red_circle.draw()
            green_circle.draw()
            black_circle.draw()
            white_circle.draw()
            yellow_circle.draw()
        elif event.type == pygame.MOUSEBUTTONUP:
            blue_circle.grow(1)
            red_circle.grow(2)
            green_circle.grow(3)
            black_circle.grow(4)
            white_circle.grow(5)
            yellow_circle.grow(6)
        elif event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            purpleCircle = Mycircle("purple", pos, 5, 0)
            purpleCircle.draw()
            pygame.display.update()



