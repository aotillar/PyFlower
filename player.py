import pygame
import random
import time
import sys


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = []
        self.image = pygame.image.load("sprites/sprite_bee0.png")
        self.images.append(pygame.image.load("sprites/sprite_bee0.png"))
        self.images.append(pygame.image.load("sprites/sprite_bee1.png"))
        self.images.append(pygame.image.load("sprites/sprite_bee2.png"))
        self.images.append(pygame.image.load("sprites/sprite_bee3.png"))
        self.images.append(pygame.image.load("sprites/sprite_bee4.png"))

        self.index = 0

        self.image = self.images[self.index]

        self.rect = self.image.get_rect()
        self.rect.center = (160, 600)

        self.direction = pygame.math.Vector2()
        self.speed = 10

        # Game Information
        self.pollen = 0

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def move(self):
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update_pollen(self):
        self.pollen += 1

    def update(self):
        self.input()
        self.rect.center += self.direction * self.speed
        self.index += 1

        # if the index is larger than the total images
        if self.index >= len(self.images):
            # we will make the index to 0 again
            self.index = 0

        # finally we will update the image that will be displayed
        self.image = self.images[self.index]
