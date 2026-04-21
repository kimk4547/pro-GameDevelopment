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



images = ["item1.png", "item2.png", "item3.png"]

for i in range(50):
    item = Recyclable(random.choice(images))

    item.rect.x = random.randrange(screen_width)

    item.rect.y = random.randrange(screen_height)

    item_list.add(item)

    allsprites.add(item)


white = (255,255,255)

red = (255,0,0)

black = (0,0,0)

green = (0,255,0)


playing = True

score = 0



clock = pygame.time.Clock()

start_time = time.time()



font = pygame.font.SysFont("comic sans", 22)

text = font.render("Score = " + str(0), True, black)



while playing:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            pygame.quit()

    
    time_elapsed = time.time() - start_time

    if time_elapsed >= 60:
        if score >= 20:
            screen.fill("green")

            text1 = font.render("Good job, you won!", True, black)
        
        else:
            screen.fill("red")

            text1 = font.render("Sorry, you lost. Try again!", True, black)

    
        screen.blit(text1,(250, 40))


    else:
        change_background("bground.png")

        countdown = font.render("Time Left : " + str(60 - int(time_elapsed)), True, black)

        
        screen.blit(countdown,(20,10)) 

        
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            if bin.rect.y > 0:
                bin.rect.y -= 5

        if keys[pygame.K_DOWN]:
            if bin.rect.y < 700:
                bin.rect.y += 5

        if keys[pygame.K_RIGHT]:
            if bin.rect.x < 900:
                bin.rect.x += 5

        if keys[pygame.K_LEFT]:
            if bin.rect.x > 0:
                bin.rect.x -= 5



        
        item_hit_list = pygame.sprite.spritecollide(bin, item_list, True)

        plastic_hit_list = pygame.sprite.spritecollide(bin, plastic_list, True)


        for item in item_hit_list:
            score += 1
            text = font.render("Score = " + str(score), True, black)

        for item in plastic_hit_list:
            score -= 5
            text = font.render("Score = " + str(score), True, black)



    
    screen.blit(text, (20, 50))

    allsprites.draw(screen)

    
    pygame.display.update()








pygame.quit()



        



        










    

