import pygame
import random
import time
import sys


class Flower(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height,pollen_ammount):
        super().__init__()
        self.images = [
            pygame.image.load("sprites/flower.png"),
            pygame.image.load("sprites/flower_red.png"),
            pygame.image.load("sprites/flower_blue.png")
        ]
        screen_width = screen_width
        screen_height = screen_height
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(32, screen_width), random.randint(32, screen_height))
        self.pollen = random.randint(1, pollen_ammount)
        self.contact = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def move(self):
        pass

    def update(self):
        if self.pollen > 0 and self.contact:
            self.pollen -= 1
            print('updating pollen')

    def update_death(self):
        pass
