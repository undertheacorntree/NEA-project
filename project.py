import pygame
from character import Character

# starts pygame
pygame.init()

# required info
bg_colour = (77,166,255)
size = (800,600) 
screen = pygame.display.set_mode(size)
pygame.display.set_caption("my project")

# settings for game loop
current_game = True
clock = pygame.time.Clock()

# game loop
while current_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            current_game = False

    screen.fill(bg_colour)

    pygame.display.flip()
    clock.tick(60)

# exit
pygame.quit()