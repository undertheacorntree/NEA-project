import pygame
from character import Character
from ground import Ground
from background import Background

# initiating pygame
pygame.init()

# game display info
bg_colour = (77,166,255)
game_title = "my project title goes here"

# setting game display to screen width
info_object = pygame.display.Info()
screen = pygame.display.set_mode((info_object.current_w, info_object.current_h))
pygame.display.set_caption(game_title)

# sprite info
character = Character((200, 300))
ground = Ground((700, 800))
background = Background((1000,1100))
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

    # display control
    screen.fill(bg_colour)      # filling in background
    background.render(screen)   # drawing on background
    ground.render(screen)       # drawing on ground
    group.draw(screen)          # drawing on sprites
    
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

# close pygame
pygame.quit()