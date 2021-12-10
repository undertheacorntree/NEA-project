import pygame, os

''' this class is used to generate the player! '''
class Player(pygame.sprite.Sprite):

    # main
    def __init__(self, x_vel, y_vel):
        super().__init__()
        self.image = pygame.image.load(os.path.join("assets", "alien_facing_left.png"))
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.rect = self.image.get_rect()
    
    # movement
    def move(self, keys_pressed, window):

        window_width = window.get_width()
        window_height = window.get_height()

        # move left
        if keys_pressed[pygame.K_a] and self.rect.x - self.x_vel > 0:
            self.rect.x -= self.x_vel

        # move right
        if keys_pressed[pygame.K_d] and self.rect.x + self.x_vel < (window_width - self.rect.width):
            self.rect.x += self.x_vel

        # move up
        if keys_pressed[pygame.K_w] and self.rect.y - self.y_vel > 0:
            self.rect.y-=self.y_vel
        
        # gravity
        else:
            self.rect.y += self.y_vel # half this later for slow fall speed, could be doubled for boots