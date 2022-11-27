import pygame
import random
import time
import sys
import math


class Bee(pygame.sprite.Sprite):
    def __init__(self, flower_list,screen_width, screen_height, hive):
        super().__init__()
        self.seek_hive = False
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
        self.rect.center = (random.randint(32, screen_width-32), random.randint(32, screen_height-32))

        self.flower_list = flower_list
        self.closest_flower = None

        self.direction = pygame.math.Vector2()
        self.speed = 10

        # Game Information
        self.pollen = 0

        self.hive = hive

        self.life_counter = 0

        self.search_distance = random.randint(50,500)

        # Use to hold floats. Since Rects are only integers.
        self.center = pygame.Vector2(self.rect.center)
        self.vector = pygame.Vector2()
        self.angle = 2

        # Test
        # self.angle = random.randint(0, 360)
        #self.check_nearest_flower()
        #self.update_vectors()


    def update_vectors(self):
        """
        We calculate the angle to the nearest flower

        :return:
        """
        self.angle = math.atan2(self.closest_flower.rect.center[1] - self.rect.center[1],
                                self.closest_flower.rect.center[0] - self.rect.center[0])

    def angle_target(self,target):
        """
        We calculate the angle to the nearest flower

        :return:
        """
        self.angle = math.atan2(target.rect.center[1] - self.rect.center[1],
                                target.rect.center[0] - self.rect.center[0])


    def check_nearest_flower(self):
        """
        dist = math.hypot(x1-x2, y1-y2)

        vector1 = pygame.Vector2(cube1.center)
        vector2 = pygame.Vector2(cube2.center)
        distance = vector1.distance_to(vector2) # returns a float.

        :return:
        """
        closest_flower = None
        self.distance = 0
        shortest_distance = 50000
        vector1 = pygame.Vector2(self.rect.center)
        for flower in self.flower_list:
            vector2 = pygame.Vector2(flower.rect.center)
            self.distance = vector1.distance_to(vector2)
            if self.distance < shortest_distance:
                shortest_distance = self.distance
                closest_flower = flower

        self.closest_flower = closest_flower

    @staticmethod
    def calculate_distance(rect1, rect2):
        vector1 = pygame.Vector2(rect1.center)
        vector2 = pygame.Vector2(rect2.center)
        distance = vector1.distance_to(vector2)
        return distance

    def move(self):
        self.check_nearest_flower()
        self.update_vectors()
        current_distance = self.calculate_distance(self.rect, self.closest_flower.rect)
        collided = pygame.sprite.spritecollide(self, self.flower_list, False)

        if current_distance >= self.search_distance:
            self.check_nearest_flower()
            self.update_vectors()

        if self.seek_hive:
            self.angle_target(self.hive)
            self.vector.from_polar((1, math.degrees(self.angle)))
            self.center += self.vector * self.speed
            self.rect.center = self.center

        elif not collided:
            self.vector.from_polar((1, math.degrees(self.angle)))
            self.center += self.vector * self.speed
            self.rect.center = self.center
            current_distance -= abs(self.vector[0] * self.speed)








        '''if current_distance > 1.0:
            self.vector.from_polar((1, math.degrees(self.angle)))
            print(self.vector*self.speed)
            self.center += self.vector * self.speed
            self.rect.center = self.center
            current_distance -= abs(self.vector[0]*self.speed)
            print('New Current Distance',current_distance)'''

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update_pollen(self):
        self.pollen += 1

    def update_hive_pollen(self):
        self.pollen -= 1

    def update(self):
        if self.pollen > 40.0:
            self.seek_hive = True
        if self.pollen <= 0:
            self.pollen = 0
            self.seek_hive = False

        self.life_counter += 1

        # Animation Code
        self.index += 1

        # if the index is larger than the total images
        if self.index >= len(self.images):
            # we will make the index to 0 again
            self.index = 0

        # finally we will update the image that will be displayed
        self.image = self.images[self.index]
