
import pygame
import random
import time
import sys

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

PI = 3.141592653

pygame.init()
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
SPEED = 5

# Set the width and height of the screen [width, height]
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites/enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.bottom > SCREEN_HEIGHT):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites/player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 600)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.top > 0:
            if pressed_keys[pygame.K_UP]:
                self.rect.move_ip(0, -10)
        if self.rect.bottom < SCREEN_HEIGHT:
            if pressed_keys[pygame.K_DOWN]:
                self.rect.move_ip(0,10)

        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-10, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(10, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Game initiliazation code
P1 = Player()
E1 = Enemy()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 10000)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == INC_SPEED:
            SPEED += 5

    # --- Game logic should go here
    P1.update()
    E1.move()

    # --- Screen-clearing code goes here


    # --- Drawing code should go here

    # --- Moves and Re-draws all Sprites
    surface.fill(WHITE)
    for entity in all_sprites:
        surface.blit(entity.image, entity.rect)
        entity.move()

        # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        surface.fill(RED)
        pygame.display.update()


    # --- Go ahead and update the screen with what we've drawn.
    #scaled_win = pygame.transform.smoothscale(surface, (SCREEN_WIDTH,SCREEN_HEIGHT))
    # or scaled_win = pygame.transform.scale(win, display_win.get_size())
    screen.blit(surface, (0, 0))
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()