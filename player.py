import pygame, os

''' this class is used to generate the player! '''
class Player(pygame.sprite.Sprite):

    # main
    def __init__(self, x_velocity):
        super().__init__()
        self.image = pygame.image.load(os.path.join("assets", "alien_facing_left.png"))
        self.x_velocity = x_velocity
        self.rect = self.image.get_rect()
    
    # movement
    def moving(self, player, keys_pressed, window_width):

        # move left
        if keys_pressed[pygame.K_a] and player.x - x_velocity > 0:
            player.x -= x_velocity

        # move right
        if keys_pressed[pygame.K_d] and player.x + x_velocity < (window_width - PLAYER_WIDTH) :
            player.x += x_velocity