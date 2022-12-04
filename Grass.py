import pygame
import random
import time
import sys


class Grass(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.images = [
            pygame.image.load("sprites/grass_blade.png"),
            pygame.image.load("sprites/grass_blade2.png"),
            pygame.image.load("sprites/grass_blade3.png")
        ]


        screen_width = screen_width
        screen_height = screen_height
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(32, screen_width-32), random.randint(32, screen_height-32))

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def move(self):
        pass

    def update(self):
        pass

    def update_death(self):
        pass
