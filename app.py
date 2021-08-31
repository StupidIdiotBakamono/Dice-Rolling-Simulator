import pygame
import pygame.draw
import pygame.font
import pygame.transform
import sys
from pygame.locals import *
import random
import pygame.mixer

pygame.init()
pygame.font.init()
pygame.mixer.init()

# Base setup
title = "Dice Rolling Simulator"
width, height = 1200, 900

FPS = 60

clock = pygame.time.Clock()

display = pygame.display.set_mode((width, height))
pygame.display.set_caption(title)


# Dices
dices = [
    pygame.image.load("assets/die1.png").convert_alpha(),
    pygame.image.load("assets/die2.png").convert_alpha(),
    pygame.image.load("assets/die3.png").convert_alpha(),
    pygame.image.load("assets/die4.png").convert_alpha(),
    pygame.image.load("assets/die5.png").convert_alpha(),
    pygame.image.load("assets/die6.png").convert_alpha(),
]
default_dice = dices[0]



# Dice Audio
dice_roll = pygame.mixer.Sound("assets/dice_roll.wav")



# Game Class
class Game():
    def __init__(self):
        self.run = 1

        self.current_dice = default_dice
        self.current_dice_rect = pygame.Rect(
            width/2 - self.current_dice.get_width()/2,
            height/2 - self.current_dice.get_height()/2,
            self.current_dice.get_width(),
            self.current_dice.get_height()
        )


        # Title
        self.title_font = pygame.font.SysFont("ComicSans", 100)
        self.title_render = self.title_font.render("Dice Rolling Simulator", True, (255,255,255))


        # Roll Button
        self.roll_button = pygame.Rect(width/2 - 300/2, height - 200, 300, 80)
        self.roll_font = pygame.font.SysFont("ComicSans", 50)
        self.roll_render = self.roll_font.render("Roll The Dice", True, (50, 50, 50))


        # Animate 
        self.animate = False

    def draw(self):
        display.fill((50,50,50))

        pygame.draw.rect(display, (255,255,255), self.roll_button)
        
        display.blit(self.roll_render, (self.roll_button.x + self.roll_render.get_width()/4 - 10, self.roll_button.y + self.roll_render.get_height() - 10))

        if self.animate:
            for dice in dices:
                display.blit(dice, (self.current_dice_rect.x, self.current_dice_rect.y))
    
            self.animate = False

        else:
            display.blit(self.current_dice, (self.current_dice_rect.x, self.current_dice_rect.y))


        display.blit(self.title_render, (width/2 - self.title_render.get_width()/2, 100))

        pygame.display.update()
    

    def start(self):
        # Game loop
        while self.run:

            mouse_pos = pygame.mouse.get_pos()
            
            clock.tick(FPS)

            self.draw()

            # Handling Events
            for event in pygame.event.get():
                # Quit Event
                if event.type == QUIT:
                    self.run = 0
                    pygame.quit()
                    sys.exit()

                if event.type == MOUSEBUTTONDOWN:
                    if self.roll_button.collidepoint(mouse_pos):
                        self.animate = True
                        dice_roll.play()
                        self.current_dice = random.choice(dices)



Game().start()
            
        