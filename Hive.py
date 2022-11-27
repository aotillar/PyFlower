import pygame
import random
import time
import sys


class Hive(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        screen_width = screen_width
        screen_height = screen_height
        self.image = pygame.image.load("sprites/Beehive.png")
        self.rect = self.image.get_rect()
        self.rect.center = (32, 64)
        self.pollen = 0
        self.honey = 0
        self.honey_timer = 0
        self.honey_store = 0
        self.contact = False
        self.bee_pop = 0
        self.honey_requirement = 0.25 * self.bee_pop + 75
        self.honey_rate = round(random.uniform(0.015, 0.5), 2)
        print(self.honey_rate)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def move(self):
        pass

    def update(self, entity, bee_list):
        self.honey_timer += 10
        if self.contact:
            if self.pollen >= 0 and entity.pollen >= 0:
                drop_pollen = entity.pollen
                self.pollen += drop_pollen
                entity.pollen = 0

        if self.pollen >= self.honey_requirement and self.honey_timer >= 120:
            self.create_honey()
            self.honey_timer = 0

        self.bee_pop = len(bee_list)

    def create_bees(self, bee_number):
        self.honey -= 150 * bee_number

    def create_bees_fromStore(self, bee_number):
        self.honey_store -= 50 * bee_number

    def create_honey(self):
        """
        In the future it would be wise to make this a function of some sort.

        x minimum pollen to create x amount of honey
        y = mx + b
        where y = pollen
        where x = honey
        where m = pollen to honey conversion rate
        where b is minimum amount of pollen to have in the hive at all times.
        :return:
        """

        if self.pollen >= self.honey_requirement:

            self.pollen -= self.honey_rate * self.bee_pop + 75
            self.honey += self.honey_rate * self.bee_pop
            self.store_honey()
            if self.pollen <= 0:
                self.pollen = 0

    def store_honey(self):
        self.honey_store += 0.5
