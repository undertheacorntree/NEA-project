import pygame
from character import Character

SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1200

# starts pygame
pygame.init()

# required info
bg_colour = (77,166,255)
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("my project")

character = Character((200,300))
group = pygame.sprite.RenderPlain()
group.add(character)

# settings for game loop
clock = pygame.time.Clock()
current_game = True

# game loop
while current_game:

    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            current_game = False

    screen.fill(bg_colour)
    group.draw(screen)
    pygame.display.flip()
    clock.tick(60)

# close pygame
pygame.quit()