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



class Healthy(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = pygame.image.load(image)

        self.image = pygame.transform.scale(self.image, (30,30))

        self.rect = self.image.get_rect()


class Unhealthy(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = pygame.image.load(image)

        self.image = pygame.transform.scale(self.image, (30,30))

        self.rect = self.image.get_rect()

healthy_list = pygame.sprite.Group()

unhealthy_list = pygame.sprite.Group()

allsprites = pygame.sprite.Group()

bodybuilder = Bodybuilder()

allsprites.add(bodybuilder)

list1 = ["carrot.png", "broccoli.png", "apple.png"]

list2 = ["chips.png", "pizza.png"]

for i in range(70):
    healthy = Healthy(random.choice(list1))

    healthy.rect.x = random.randrange(screen_width)    

    healthy.rect.y = random.randrange(screen_height)

    healthy_list.add(healthy)

    allsprites.add(healthy) 

for i in range(20):
    unhealthy = Unhealthy(random.choice(list2))

    unhealthy.rect.x = random.randrange(screen_width)    

    unhealthy.rect.y = random.randrange(screen_height)

    unhealthy_list.add(unhealthy)

    allsprites.add(unhealthy) 


white = (255,255,255)

red = (255,0,0)

black = (0,0,0)

green = (0,255,0)


playing = True

score = 0



clock = pygame.time.Clock()

start_time = time.time()



font = pygame.font.SysFont("comic sans", 22)

text = font.render("Score = " +str(0), True, black)



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


        screen.blit(text1,(250,40))


    else:
        change_background("gymbg.jpeg")

        countdown = font.render("Time Left : " + str(60 - int(time_elapsed)), True, black)

        
        screen.blit(countdown,(20,10)) 



        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            if bodybuilder.rect.y > 0:
                bodybuilder.rect.y -= 5

        if keys[pygame.K_DOWN]:
            if bodybuilder.rect.y < 700:
                bodybuilder.rect.y += 5

        if keys[pygame.K_RIGHT]:
            if bodybuilder.rect.x < 900:
                bodybuilder.rect.x += 5

        if keys[pygame.K_LEFT]:
            if bodybuilder.rect.x > 0:
                bodybuilder.rect.x -= 5




        healthy_hit_list = pygame.sprite.spritecollide(bodybuilder, healthy_list, True)

        unhealthy_hit_list = pygame.sprite.spritecollide(bodybuilder, unhealthy_list, True)
        

        for item in healthy_hit_list:
            score += 1
            text = font.render("Score = " + str(score), True, black)

        for item in unhealthy_hit_list:
            score -= 5
            text = font.render("Score = " + str(score), True, black)




    screen.blit(text, (20,50))

    allsprites.draw(screen)


    pygame.display.update()








pygame.quit()












    
