import pygame
pygame.init()

screen_width = 500
screen_height = 700

screen = pygame.display.set_mode([screen_width, screen_height])

class Player(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image = pygame.image.load("spaghetti.jpeg")
        self.image = pygame.transform.scale(self.image,(70,100))
        self.rect = self.image.get_rect()

    def update(self, pressed_keys):
        if (pressed_keys[pygame.K_UP]):
            self.rect.move_ip(0,-5)
        if (pressed_keys[pygame.K_DOWN]):
            self.rect.move_ip(0,5)
        if (pressed_keys[pygame.K_RIGHT]):
            self.rect.move_ip(5,0)
        if (pressed_keys[pygame.K_LEFT]):
            self.rect.move_ip(-5,0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 500:
            self.rect.right = 500
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 700:
            self.rect.bottom = 700

sprites = pygame.sprite.Group()

def StartGame():
    food1 = Player()
    sprites.add(food1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
    
        pressed_keys = pygame.key.get_pressed()

        food1.update(pressed_keys)

        bg = pygame.image.load("fridge.jpeg") 
        bg = pygame.transform.scale(bg,(500,700))
        screen.blit(bg, (0,0))

        sprites.draw(screen)

        pygame.display.update()

StartGame()