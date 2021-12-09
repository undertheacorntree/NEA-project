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
    def move(self, keys_pressed, window):

        window_width = window.get_width()
        window_height = window.get_height()

        # move left
        if keys_pressed[pygame.K_a] and self.rect.x - self.x_velocity > 0:
            self.rect.x -= self.x_velocity

        # move right
        if keys_pressed[pygame.K_d] and self.rect.x + self.x_velocity < (window_width - self.rect.width):
            self.rect.x += self.x_velocity