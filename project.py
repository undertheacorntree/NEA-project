# yikes chief we've got a problem on our hands
import pygame, os
from player import Player

# IMPORTANT GAME INFOMATION
pygame.display.set_caption("my project title goes here")
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 1000
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
BASE_COLOUR = (77,166,255)
FPS = 60

# PLATFORM INFORMATION
# creates rect at (x pos/y pos) (width/height)
first_platform = pygame.Rect((200,900),(130,30))

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

    # this draws the first (white) platform to the window
    pygame.draw.rect(WINDOW, (255,255,255), first_platform)

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
        player.move(keys_pressed, WINDOW)    

        # whoo game !!!!!
        draw_window()

    pygame.quit()

# RUNS FILE
if __name__ == "__main__":
    main()