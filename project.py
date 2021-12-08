import pygame, os
from character import Character
from ground import Ground

# important game information
WINDOW_WIDTH, WINDOW_HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
BASE_COLOUR = (77,166,255)
FPS = 60
VELOCITY = 4

pygame.display.set_caption("my project title goes here")
player_img_path = "alien_facing_left.png"
PLAYER_IMG = pygame.image.load(os.path.join("assets", player_img_path))
PLAYER_WIDTH, PLAYER_HEIGHT = 66, 92

# creating screen
def draw_window(player):
    WINDOW.fill(BASE_COLOUR)
    WINDOW.blit(PLAYER_IMG, (player.x, player.y))
    pygame.display.update()

# movement
def player_movement(keys_pressed, player):

    # move left
        if keys_pressed[pygame.K_a] and player.x - VELOCITY > 0:
            player.x -= VELOCITY

        # move right
        if keys_pressed[pygame.K_d] and player.x + VELOCITY < (WINDOW_WIDTH - PLAYER_WIDTH) :
            player.x += VELOCITY

# main game loop
def main():
    player = pygame.Rect(700, 300, PLAYER_WIDTH, PLAYER_HEIGHT)

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
        player_movement(keys_pressed, player)    

        draw_window(player)
    pygame.quit

# runs file
if __name__ == "__main__":
    main()