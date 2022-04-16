# yikes chief we've got a problem on our hands
from tkinter import image_names
import pygame, os
from podium import Podium
from pickup import Pickup
from player import Player

# IMPORTANT GAME INFOMATION
pygame.display.set_caption("my project title goes here")
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 1000
MENU_X, MENU_Y = 10, 10
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
BASE_COLOUR = (77,166,255)
FPS = 60

# PLATFORM INFORMATION
# passes in image, x-pos, y-pos
platform_a = Podium("platform_default.png", 300, 950)
platform_b = Podium("platform_alt.png", 600, 850)
platform_c = Podium("platform_default.png", 300, 750)
platform_d = Podium("platform_alt.png", 600, 650)
platform_e = Podium("platform_alt.png", 300, 550)
platform_f = Podium("platform_default.png", 600, 450)
platform_g = Podium("platform_default.png", 300, 350)
platform_h = Podium("platform_special.png", 600, 250)

# create list
platforms = [platform_a, platform_b, platform_c, platform_d, platform_e, platform_f, platform_g, platform_h] 

# ITEM INFORMATION
# passes in x-pos, y-pos
item_heavy_boots = Pickup('heavy_boots.png', False, platform_b.rect.x + 50, platform_b.rect.y - platform_b.rect.height - 1)
item_speedy_boots = Pickup('speedy_boots.png', False, platform_c.rect.x + 50, platform_c.rect.y - platform_c.rect.height - 1)
item_exploding_flower = Pickup('exploding_flower.png', False, platform_f.rect.x + 50, platform_f.rect.y - platform_f.rect.height - 1)
item_no_item = Pickup('no_item.png', True, MENU_X, MENU_Y)

# create lists
items_available = [item_heavy_boots, item_speedy_boots, item_exploding_flower]
items_gained = [item_no_item]

# SPRITE INFORMATION
sprite_group = pygame.sprite.Group()
# stores images in order: left, right
image_names = ["alien_left.png","alien_right.png"]

# this passes in the image, x-velocity, y-velocity
# starting postions (x,y), jump height
player = Player(image_names, 10, 0, 100, 100, 15, 1)
sprite_group.add(player)

# CREATE SCREEN
def draw_window():

    # whooo background whooooo
    WINDOW.fill(BASE_COLOUR)

    # this draws the platforms to the window
    for platform in platforms:
        WINDOW.blit(platform.image, (platform.rect.x, platform.rect.y))

    # this draws the items available to the window
    for item in items_available:        
        WINDOW.blit(item.image, (item.rect.x, item.rect.y))
    
    # this draws the items gained to the window
    for item in items_gained:
        if item.item_selected == True:
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

            # check for specific key presses
            if event.type == pygame.KEYDOWN:

                # inventory access
                if (event.key == pygame.K_q) and (len(items_gained) > 1):
                    player.item_select(items_gained, platforms)
                
                # jumping
                if (event.key == pygame.K_w) and (player.falling == False):
                    player.jumping = True

                # start moving left
                if (event.key == pygame.K_a):
                    player.moving_left = True
                    player.image = pygame.image.load(os.path.join("assets", image_names[0]))

                # start moving right
                if (event.key == pygame.K_d):
                    player.moving_right = True
                    player.image = pygame.image.load(os.path.join("assets", image_names[1]))

            # stop continued action
            if event.type == pygame.KEYUP:

                # stop moving left
                if (event.key == pygame.K_a):
                    player.moving_left = False

                # stop moving right
                if (event.key == pygame.K_d):
                    player.moving_right = False

        # make the sprite move
        player.move(WINDOW, MENU_X, MENU_Y, platforms, items_available, items_gained)
        
        # whoo game !!!!!
        draw_window()

    # quit game
    pygame.quit()

# RUNS FILE
if __name__ == "__main__":
    main()