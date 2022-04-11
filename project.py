# yikes chief we've got a problem on our hands
import pygame, os
from player import Player
from podium import Podium

# IMPORTANT GAME INFOMATION
pygame.display.set_caption("my project title goes here")
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 1000
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
BASE_COLOUR = (77,166,255)
FPS = 60

# PLATFORM INFORMATION
# passes in image, x-pos, y-pos
platform_a = Podium("platform.png", 200, 900)
platform_b = Podium("platform.png", 300, 800)

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

    # this draws the first platform to the window
    WINDOW.blit(platform_a.image, (platform_a.rect.x, platform_a.rect.y))
    WINDOW.blit(platform_b.image, (platform_b.rect.x, platform_b.rect.y))

    # sprite group tings
    sprite_group.update()
    sprite_group.draw(WINDOW)

    # updates the window
    pygame.display.update()
    
# MAIN GAME LOOP
def main():

    # EVENT LOOP
    clock = pygame.time.Clock()
    current_game = True

    while current_game:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_game = False

        # checking for pressed keys
        keys_pressed = pygame.key.get_pressed()
        player.move(keys_pressed, WINDOW, platform_a)    

        # whoo game !!!!!
        draw_window()

    pygame.quit()

# RUNS FILE
if __name__ == "__main__":
    main()