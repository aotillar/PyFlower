import pygame
import random
import time
import sys
from flower import *
from player import *
from Bee import *
from Hive import *

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 254)
BLUE = (0, 0, 255)
GREEN = (0, 155, 50)
RED = (255, 0, 0)

# test comment
PI = 3.141592653

pygame.init()
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

# Set the width and height of the screen [width, height]
infoObject = pygame.display.Info()

size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
# surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
surface = pygame.Surface((infoObject.current_w, infoObject.current_h))

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# User events


# Game initiliazation code

def create_flowers(num_flowers):
    for entitiy in range(num_flowers):
        entitiy = Flower(
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            25
        )
        flowers.add(entitiy)


def create_bees(num_bees):
    for entity in range(num_bees):
        entity = Bee(flowers,
                     SCREEN_WIDTH,
                     SCREEN_HEIGHT,
                     hive)
        bees.add(entity)


player = Player()
all_sprites = pygame.sprite.Group()
flowers = pygame.sprite.Group()
bees = pygame.sprite.Group()
hive = Hive(SCREEN_WIDTH, SCREEN_HEIGHT)

create_flowers(50)
create_bees(15)

all_sprites.add(player)

# load font, prepare values
font = pygame.font.Font(None, 32)


def show_player_score(x, y):
    score = font.render("Player Pollen :" + str(player.pollen), True, (0, 0, 0))
    screen.blit(score, (x, y))


def show_hive_score(x, y):
    score = font.render("Hive Pollen :" + str(hive.pollen), True, (0, 0, 0))
    screen.blit(score, (x, y))


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.K_ESCAPE:
            done = True
        if event.type == flower_timer:
            flower_chance = random.randint(0, 20)

    # --- Game logic should go here
    # player.update()
    all_sprites.update()
    flowers.update()
    bees.update()

    if len(flowers) == 0:
        create_flowers(25)

    # --- Screen-clearing code goes here

    # --- Drawing code should go here

    # --- Moves and Re-draws all Sprites
    surface.fill(GREEN)

    surface.blit(hive.image, hive.rect)

    for entity in flowers:
        surface.blit(entity.image, entity.rect)
        entity.move()

    for entity in all_sprites:
        surface.blit(entity.image, entity.rect)
        entity.move()

    for entity in bees:
        surface.blit(entity.image, entity.rect)
        entity.move()

    # To be run if collision occurs between Player and Flower
    # check if the bee has collided with the flowers, and if so
    # remove the pollen from the flower and add it to the bee.

    # Check if AI bees are colliding with flowers, if so remove pollen from flowers and add it to Bees.
    for bee in bees:
        if pygame.sprite.spritecollide(bee, flowers, False):
            collided = pygame.sprite.spritecollide(bee, flowers, False)
            collided[0].contact = True
            if collided[0].pollen > 0:
                collided[0].update()
                bee.update_pollen()
            pygame.display.update()
        else:
            for entity in flowers:
                entity.contact = False

    # Check player flower collisoin and update pollen
    if pygame.sprite.spritecollide(player, flowers, False):
        collided = pygame.sprite.spritecollide(player, flowers, False)
        collided[0].contact = True
        if collided[0].pollen > 0:
            collided[0].update()
            player.update_flower_pollen()
        pygame.display.update()
    else:
        for entity in flowers:
            entity.contact = False

    # Check for Player Hive Collision
    if pygame.sprite.collide_rect(player, hive):
        hive.contact = True
        if player.pollen > 0:
            hive.update(player)
            player.update_hive_pollen()
        pygame.display.update()
    else:
        hive.contact = False

    # Check for bee Hive Collision
    if pygame.sprite.spritecollide(hive, bees, False):
        collided = pygame.sprite.spritecollide(hive, bees, False)
        hive.contact = True
        if collided[0].pollen > 0:
            hive.update(collided[0])
            collided[0].update_hive_pollen()
        pygame.display.update()
    else:
        hive.contact = False

    for entity in flowers:
        if entity.pollen == 0:
            flowers.remove(entity)

    # --- Go ahead and update the screen with what we've drawn.
    # scaled_win = pygame.transform.smoothscale(surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
    # or scaled_win = pygame.transform.scale(win, display_win.get_size())
    screen.blit(surface, (0, 0))
    show_player_score(15, 15)
    show_hive_score(260, 15)

    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(24)

# Close the window and quit.
pygame.quit()
