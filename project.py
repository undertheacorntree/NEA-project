# yikes chief we've got a problem on our hands
import pygame, os
from player import Player

# IMPORTANT GAME INFOMATION
WINDOW_WIDTH, WINDOW_HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
BASE_COLOUR = (77,166,255)
FPS = 60

pygame.display.set_caption("my project title goes here")

# SPRITE INFORMATION
sprite_group = pygame.sprite.Group()

# this passes in the image, x-velocity, y-velocity
# starting postions (x,y), jump height
player = Player("alien_facing_left.png", 5, 0, 100, 100, 15)
sprite_group.add(player)

# CREATE SCREEN
def draw_window():
    WINDOW.fill(BASE_COLOUR)
    sprite_group.update()
    sprite_group.draw(WINDOW)
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
        player.move(keys_pressed, WINDOW)    

        draw_window()

    pygame.quit()

# RUNS FILE
if __name__ == "__main__":
    main()