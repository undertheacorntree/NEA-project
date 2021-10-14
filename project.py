import pygame, os
from character import Character
from ground import Ground

# initiating
pygame.init()   

# important game info
base_colour = (77,166,255) # might be removed later
picture = pygame.image.load(os.path.join("assets", "test_background.png"))

# setting game display to screen width
info_object = pygame.display.Info()
resolution = (info_object.current_w, info_object.current_h)
screen = pygame.display.set_mode(resolution)

pygame.display.set_caption("my project title goes here")

# sprite info
character = Character((300, 200), "alien_facing_right.png")
foreground = Ground((700, 800), "test_foreground.png")
sprite_group = pygame.sprite.RenderPlain()
sprite_group.add(character)

# settings for game loop & fps
clock = pygame.time.Clock()
current_game = True

# game loop
while current_game:

    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            current_game = False

    # display control
    screen.fill(base_colour)    # filling in background

    
    # background = pygame.transform.scale(picture, (resolution))
    
    foreground.render(screen)   # drawing on foreground
    sprite_group.draw(screen)   # drawing on sprites
    
    
    # movement for sprite
    keys = pygame.key.get_pressed()
    
    # going left
    if keys[pygame.K_a]:
        character.move_left(5)

    # going right
    if keys[pygame.K_d]:
        character.move_right(5)

    # updating screen
    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()

# close pygame
pygame.quit()