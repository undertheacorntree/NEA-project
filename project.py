import pygame, os
from player import Player

# important game information
WINDOW_WIDTH, WINDOW_HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
BASE_COLOUR = (77,166,255)
FPS = 60

pygame.display.set_caption("my project title goes here")

# sprite info 
# yikes
sprite_group = pygame.sprite.Group()
player = Player(4)
sprite_group.add(player)

# creating screen
def draw_window(player):
    WINDOW.fill(BASE_COLOUR)
    sprite_group.update()
    sprite_group.draw(WINDOW)
    pygame.display.update()

# main game loop
def main():

    # event loop
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

        draw_window(player)

    pygame.quit()

# runs file
if __name__ == "__main__":
    main()