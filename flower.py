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
            pygame.image.load("sprites/flower_blue.png"),
            pygame.image.load("sprites/flower_8petal.png"),
            pygame.image.load("sprites/flower_pink.png"),
            pygame.image.load("sprites/flower_turquiose.png"),
            pygame.image.load("sprites/flower_umber.png"),
            pygame.image.load("sprites/flower_yellow.png"),
            pygame.image.load("sprites/4petal_flower.png"),
            pygame.image.load("sprites/cactus_1.png"),
            pygame.image.load("sprites/flower_pink.png"),
            pygame.image.load("sprites/grass_flowers.png"),
            pygame.image.load("sprites/small_blue_flower.png"),
            pygame.image.load("sprites/small_red_flower.png")
        ]
        screen_width = screen_width
        screen_height = screen_height
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(32, screen_width-32), random.randint(32, screen_height-32))
        self.pollen = random.randint(1, pollen_ammount)
        self.contact = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def move(self):
        pass

    def update(self):
        if self.pollen > 0 and self.contact:
            self.pollen -= 1

    def update_death(self):
        pass
