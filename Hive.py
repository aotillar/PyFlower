import pygame
import random
import time
import sys


class Hive(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        screen_width = screen_width
        screen_height = screen_height
        self.image =  pygame.image.load("sprites/Beehive.png")
        self.rect = self.image.get_rect()
        self.rect.center = (32,64)
        self.pollen = 0
        self.contact = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def move(self):
        pass

    def update(self, entity):
        if self.contact:
            if self.pollen >= 0 and entity.pollen >=0:
                self.pollen += entity.pollen

    def create_new_bee:
        self.pollen -= 250
