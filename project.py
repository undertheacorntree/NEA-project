# yikes chief we've got a problem on our hands
import pygame, os
from podium import Podium
from pickup import Pickup
from player import Player

# IMPORTANT GAME INFOMATION
pygame.display.set_caption("my project title goes here")
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 1000
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
BASE_COLOUR = (77,166,255)
FPS = 60

# PLATFORM INFORMATION
# passes in image, x-pos, y-pos
platform_a = Podium("platform.png", 200, 950)
platform_b = Podium("platform.png", 500, 850)
platform_c = Podium("platform.png", 200, 750)
platform_d = Podium("platform.png", 500, 650)
platforms = [platform_a, platform_b, platform_c, platform_d] 

# ITEM INFORMATION
# passes in x-pos, y-pos
item_a = Pickup(platform_b.rect.x + 50, platform_b.rect.y - platform_b.rect.height - 10)
item_b = Pickup(platform_c.rect.x + 50, platform_c.rect.y - platform_c.rect.height - 10)
items = [item_a, item_b]

# SPRITE INFORMATION
sprite_group = pygame.sprite.Group()

# this passes in the image, x-velocity, y-velocity
# starting postions (x,y), jump height
player = Player("alien_facing_left.png", 10, 0, 100, 100, 15)
sprite_group.add(player)

# CREATE SCREEN
def draw_window():

    # whooo background whooooo
    WINDOW.fill(BASE_COLOUR)

    # this draws the platforms to the window
    for platform in platforms:
        WINDOW.blit(platform.image, (platform.rect.x, platform.rect.y))

    # this draws the items to the window
    for item in items:
        WINDOW.blit(item.image, (item.rect.x, item.rect.y))

    # sprite group tings
    sprite_group.update()
    sprite_group.draw(WINDOW)

    # updates the window
    pygame.display.update()
    
# MAIN GAME LOOP
def main():

    # game loop info
    clock = pygame.time.Clock()
    current_game = True

    # GAME LOOP
    while current_game:
        clock.tick(FPS)

        # EVENT LOOP
        for event in pygame.event.get():

            # quit game event
            if event.type == pygame.QUIT:
                current_game = False

        # checking for pressed keys
        keys_pressed = pygame.key.get_pressed()
        player.move(keys_pressed, WINDOW, platforms)    

        # whoo game !!!!!
        draw_window()

    # quit game
    pygame.quit()

# RUNS FILE
if __name__ == "__main__":
    main()