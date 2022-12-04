import pygame
import random
import time
import sys
from flower import *
from player import *
from Bee import *
from Hive import *
from Grass import *


class BeeSim():
    def __init__(self):
        # Define some colors


        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 254)
        self.BLUE = (0, 0, 255)
        self.GREEN = (72, 125, 22)
        self.RED = (255, 0, 0)

        self.PI = 3.141592653

        pygame.init()
        self.SCREEN_WIDTH = 1080
        self.SCREEN_HEIGHT = 720

        # Set the width and height of the screen [width, height]
        infoObject = pygame.display.Info()

        self.size = (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.screen = pygame.display.set_mode(self.size)
        self.surface = pygame.Surface((infoObject.current_w, infoObject.current_h))

        pygame.display.set_caption("PyFlower")

        self.done = False

        # Game Code Init
        self.frames_per_day_counter = 0
        self.frames_per_day = 3000
        self.day_counter = 0

        self.flower_pollen_upper = 60
        self.bee_life_limit = 1200


        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()


    def create_flowers(self,num_flowers):
        for entitiy in range(num_flowers):
            entitiy = Flower(
                self.SCREEN_WIDTH,
                self.SCREEN_HEIGHT,
                self.flower_pollen_upper
            )
            self.flowers.add(entitiy)

    def create_bees(self,num_bees):
        for entity in range(num_bees):
            entity = Bee(self.flowers,
                         self.SCREEN_WIDTH,
                         self.SCREEN_HEIGHT,
                         self.hive)
            self.bees.add(entity)

    def create_grass(self,grass_num):
        for entity in range(grass_num):
            entity = Grass(self.SCREEN_WIDTH,
                           self.SCREEN_HEIGHT)
            self.grass.add(entity)
    def show_player_score(self, x, y):
        score = self.font.render("Player Pollen :" + str(self.player.pollen), True, (0, 0, 0))
        self.screen.blit(score, (x, y))

    def show_hive_score(self, x, y):
        score = self.font.render("Hive Pollen :" + str(round(self.hive.pollen,2)), True, (0, 0, 0))
        self.screen.blit(score, (x, y))

    def show_hive_pop(self, x, y):
        score = self.font.render("Hive Population :" + str(len(self.bees)), True, (0, 0, 0))
        self.screen.blit(score, (x, y))

    def show_day_counter(self, x, y):
        score = self.font.render("Day :" + str(self.day_counter), True, (0, 0, 0))
        self.screen.blit(score, (x, y))

    def show_honey_counter(self, x, y):
        score = self.font.render("Honey :" + str(round(self.hive.honey,2)), True, (0, 0, 0))
        self.screen.blit(score, (x, y))

    def show_honey_store(self, x, y):
        score = self.font.render("Honey Store:" + str(round(self.hive.honey_store,2)), True, (0, 0, 0))
        self.screen.blit(score, (x, y))

    def initialize_game(self, bee_number, flower_number):
        self.player = Player()
        self.all_sprites = pygame.sprite.Group()
        self.flowers = pygame.sprite.Group()
        self.grass = pygame.sprite.Group()
        self.bees = pygame.sprite.Group()
        self.hive = Hive(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

        self.create_flowers(bee_number)
        self.create_bees(flower_number)
        self.all_sprites.add(self.player)
        self.create_grass(125)

        self.font = pygame.font.Font(None, 32)

    def main_loop(self):
        while not self.done:
            # --- Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                if event.type == pygame.K_ESCAPE:
                    self.done = True

            # --- Game logic should go here
            # player.update()
            self.all_sprites.update()
            self.flowers.update()
            self.bees.update()
            self.hive.update(self.player, self.bees)

            if len(self.flowers) == 0:
                self.create_flowers(50)

            # This doesnt belong here

            if self.hive.honey >= self.hive.honey_per_bee:
                self.hive.create_bees(1)
                self.create_bees(1)

            # --- Screen-clearing code goes here

            # --- Drawing code should go here

            # --- Moves and Re-draws all Sprites
            self.surface.fill(self.GREEN)

            self.surface.blit(self.hive.image, self.hive.rect)

            for entity in self.grass:
                self.surface.blit(entity.image,entity.rect)

            for entity in self.flowers:
                self.surface.blit(entity.image, entity.rect)
                entity.move()

            for entity in self.all_sprites:
                # surface.blit(entity.image, entity.rect)
                entity.move()

            for entity in self.bees:
                self.surface.blit(entity.image, entity.rect)
                entity.move()



            # To be run if collision occurs between Player and Flower
            # check if the bee has collided with the flowers, and if so
            # remove the pollen from the flower and add it to the bee.

            # Check if AI bees are colliding with flowers, if so remove pollen from flowers and add it to Bees.
            for bee in self.bees:
                if pygame.sprite.spritecollide(bee, self.flowers, False):
                    collided = pygame.sprite.spritecollide(bee, self.flowers, False)
                    collided[0].contact = True
                    if collided[0].pollen > 0:
                        collided[0].update()
                        bee.update_pollen()
                    pygame.display.update()
                else:
                    for entity in self.flowers:
                        entity.contact = False

            # Check player flower collisoin and update pollen
            if pygame.sprite.spritecollide(self.player, self.flowers, False):
                collided = pygame.sprite.spritecollide(self.player, self.flowers, False)
                collided[0].contact = True
                if collided[0].pollen > 0:
                    collided[0].update()
                    self.player.update_flower_pollen()
                pygame.display.update()
            else:
                for entity in self.flowers:
                    entity.contact = False

            # Check for Player Hive Collision
            if pygame.sprite.collide_rect(self.player, self.hive):
                self.hive.contact = True
                if self.player.pollen > 0:
                    self.hive.update(player, bees)
                    # player.update_hive_pollen()
                pygame.display.update()
            else:
                self.hive.contact = False

            # Check for bee Hive Collision
            if pygame.sprite.spritecollide(self.hive, self.bees, False):
                collided = pygame.sprite.spritecollide(self.hive, self.bees, False)
                self.hive.contact = True
                if collided[0].pollen > 0:
                    self.hive.update(collided[0], self.bees)
                    # collided[0].update_hive_pollen()
                pygame.display.update()
            else:
                self.hive.contact = False

            # Remove entities that have been around too long

            for entity in self.flowers:
                if entity.pollen == 0:
                    chance = random.randint(0, 20)
                    if chance >= 3:
                        self.create_flowers(1)

                    self.flowers.remove(entity)

            for entity in self.bees:
                if entity.life_counter >= self.bee_life_limit:
                    self.bees.remove(entity)

            # Use Stored Honey
            if len(self.bees) == 1:
                print('MAKING BEES FROM HONEY-#-#-#-#-#-#')
                able_toMake = int(self.hive.honey_store / self.hive.bee_honey_from_store)
                self.hive.create_bees_fromStore(able_toMake)
                self.create_bees(able_toMake)
                print(able_toMake)
            elif len(self.bees) == 0:
                print("Total Days This Gen: ", self.day_counter)
                self.initialize_game(15,15)
                self.day_counter = 0
                self.frames_per_day_counter = 0

            # --- Go ahead and update the screen with what we've drawn.
            # scaled_win = pygame.transform.smoothscale(surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
            # or scaled_win = pygame.transform.scale(win, display_win.get_size())
            self.screen.blit(self.surface, (0, 0))
            self.show_player_score(15, 15)
            self.show_hive_score(260, 15)
            self.show_hive_pop(480, 15)
            self.show_day_counter(760, 15)
            self.show_honey_counter(260, 45)
            self.show_honey_store(480, 45)

            pygame.display.flip()

            # --- Limit to 24 frames per second

            self.frames_per_day_counter += 1
            if self.frames_per_day_counter >= self.frames_per_day:
                self.day_counter += 1
                self.frames_per_day_counter = 0

            self.clock.tick(60)


sim = BeeSim()
sim.initialize_game(50,15)
sim.main_loop()