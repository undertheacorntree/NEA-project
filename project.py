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
platform_a = Podium("platform.png", 300, 950)
platform_b = Podium("platform.png", 600, 850)
platform_c = Podium("platform.png", 300, 750)
platform_d = Podium("platform.png", 600, 650)
platform_e = Podium("platform.png", 300, 550)
platform_f = Podium("platform.png", 600, 450)
platform_g = Podium("platform.png", 300, 350)
platform_h = Podium("platform.png", 600, 250)
platform_i = Podium("platform.png", 100, 850)
platforms = [platform_a, platform_b, platform_c, platform_d, platform_e, platform_f, platform_g, platform_h, platform_i] 

# ITEM INFORMATION
# passes in x-pos, y-pos
item_heavy_boots = Pickup('heavy_boots.png', False, platform_b.rect.x + 50, platform_b.rect.y - platform_b.rect.height - 1)
item_speedy_boots = Pickup('speedy_boots.png', False, platform_c.rect.x + 50, platform_c.rect.y - platform_c.rect.height - 1)
item_exploding_flower = Pickup('exploding_flower.png', False, platform_f.rect.x + 50, platform_f.rect.y - platform_f.rect.height - 1)
item_no_item = Pickup('no_item.png', True, 0, 0)
items = [item_heavy_boots, item_speedy_boots, item_exploding_flower]

# SPRITE INFORMATION
sprite_group = pygame.sprite.Group()

# this passes in the image, x-velocity, y-velocity
# starting postions (x,y), jump height
player = Player("alien_facing_left.png", 10, 0, 100, 100, 15, 1)
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
        if item.item_collected == True:
            items.remove(item)
        
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
        player.move(keys_pressed, WINDOW, platforms, items)    

        # whoo game !!!!!
        draw_window()

    # quit game
    pygame.quit()

# RUNS FILE
if __name__ == "__main__":
    main()