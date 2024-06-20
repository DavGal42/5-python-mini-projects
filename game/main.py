"""
    Author_LABEL: David Galstyan
    Description: A simple game
"""

import random
import pygame


pygame.init()

GAME_SCREEN = pygame.display.set_mode((253, 450))
pygame.display.set_caption('Adventure Game')

ICON = pygame.image.load('imgs/joystick.png')
pygame.display.set_icon(ICON)

BACKGROUND_IMAGE = pygame.image.load('imgs/background.jpg')

BASKET = pygame.image.load('imgs/basket.png')
BASKET_SPEED = 0.1
BASKET_X = 100
BASKET_Y = 412

COIN = pygame.image.load('imgs/coin.png')
BOMB = pygame.image.load('imgs/bomb.png')
FALLING_SPEED = 0.1

LABEL1 = pygame.font.Font('fonts/Jersey15-Regular.ttf', 50)
LABEL2 = pygame.font.Font('fonts/Jersey15-Regular.ttf', 30)
LABEL3 = pygame.font.Font('fonts/Jersey15-Regular.ttf', 20)

LOSE_LABEL = LABEL1.render('You Lose!', True, 'White')
RESTART_LABEL = LABEL1.render('Play Again', True, (25, 100, 156))
RESTART_LABEL_RECT = RESTART_LABEL.get_rect(topleft=(40, 280))

SOUND = pygame.mixer.Sound('sounds/bg-sound.mp3')
SOUND.play()

GAME_ACTIVE = True
SCORE = 0

class FallingObject:
    """
        Description: Class of falling objects
    """
    def __init__(self, image, x, y, speed):
        """
            Description: Initialize function

            Parameters: Image of objects,their coordinates and speed
        """
        self.image = image
        self.x = x
        self.y = y
        self.speed = speed
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        """
            Description: Change position of the falling object
        """
        self.y += self.speed
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        """
            Description: Show an object on the screen

            Parameters: Main screen
        """
        screen.blit(self.image, (self.x, self.y))

falling_objects = []

def spawn_falling_object():
    """
        Description: There we open the file and read it
    """
    if random.randint(0, 3) != 0:
        falling_objects.append(FallingObject(COIN, random.randint(
            0, 253 - COIN.get_width()), 0, FALLING_SPEED))
    else:
        falling_objects.append(FallingObject(BOMB, random.randint(
            0, 253 - BOMB.get_width()), 0, FALLING_SPEED))

pygame.time.set_timer(pygame.USEREVENT, 2000)

RUNNING = True

while RUNNING:
    GAME_SCREEN.blit(BACKGROUND_IMAGE, (0, 0))

    if GAME_ACTIVE:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            BASKET_X -= BASKET_SPEED

        if keys[pygame.K_RIGHT]:
            BASKET_X += BASKET_SPEED

        if BASKET_X < 0:
            BASKET_X = 0
        elif BASKET_X > 253 - BASKET.get_width():
            BASKET_X = 253 - BASKET.get_width()

        GAME_SCREEN.blit(BASKET, (BASKET_X, BASKET_Y))

        for obj in falling_objects[:]:
            obj.update()
            obj.draw(GAME_SCREEN)

            if obj.rect.colliderect(BASKET.get_rect(topleft=(BASKET_X, BASKET_Y))):
                falling_objects.remove(obj)

                if obj.image == BOMB:
                    GAME_ACTIVE = False
                elif obj.image == COIN:
                    SCORE += 1

            elif obj.y > 450:
                falling_objects.remove(obj)

        SCORE_TEXT = LABEL2.render(f'Score: {SCORE}', True, 'White')
        GAME_SCREEN.blit(SCORE_TEXT, (10, 10))

    else:
        GAME_SCREEN.fill((25, 156, 156))
        GAME_SCREEN.blit(LOSE_LABEL, (45, 100))
        GAME_SCREEN.blit(RESTART_LABEL, RESTART_LABEL_RECT)

        FINAL_SCORE_TEXT = LABEL2.render(f'Score: {SCORE}', True, 'White')
        GAME_SCREEN.blit(FINAL_SCORE_TEXT, (80, 150))

        MOUSE = pygame.mouse.get_pos()

        if RESTART_LABEL_RECT.collidepoint(MOUSE) and pygame.mouse.get_pressed()[0]:
            GAME_ACTIVE = True
            falling_objects.clear()
            SCORE = 0
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
            pygame.quit()
        elif event.type == pygame.USEREVENT and GAME_ACTIVE:
            spawn_falling_object()
