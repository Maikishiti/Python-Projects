from globals import pygame
from player  import Player

# GLOBALS
SCREEN_SIZE = (600, 400)
SCREEN      = pygame.display.set_mode(SCREEN_SIZE)
clock       = pygame.time.Clock()

background  = pygame.image.load("Assets/Debug/32px_bg.png")

p = Player(( SCREEN_SIZE[0]/2,  SCREEN_SIZE[1]/2),  (16, 16), "Assets/Character.png", (3, 3))
p.animation_speed = 120

player_group = pygame.sprite.Group(p)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    p.key_input(pygame.key.get_pressed())
    for j in range((int)(SCREEN_SIZE[1]/background.get_size()[1]) + 1):
        for i in range((int)(SCREEN_SIZE[0]/background.get_size()[0]) + 1):
            SCREEN.blit(background, (i * background.get_size()[0], j * background.get_size()[1]))

    player_group.update()
    player_group.draw(SCREEN)


    pygame.display.update()
    clock.tick(60)

pygame.quit()
