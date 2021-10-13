import pygame
from character import Character

# initiating pygame
pygame.init()

# game display info
bg_colour = (77,166,255)
pygame.display.set_caption("my project title goes here")

# setting game display to screen width
info_object = pygame.display.Info()
screen = pygame.display.set_mode((info_object.current_w, info_object.current_h))

# sprite info
character = Character((200,300))
group = pygame.sprite.RenderPlain()
group.add(character)

# settings for game loop & fps
clock = pygame.time.Clock()
current_game = True

# game loop
while current_game:

    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            current_game = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        character.move_left(5)
    if keys[pygame.K_d]:
        character.move_right(5)

    # display control
    screen.fill(bg_colour)
    group.draw(screen)
    pygame.display.flip()
    clock.tick(60)

# close pygame
pygame.quit()