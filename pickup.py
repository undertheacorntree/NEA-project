import pygame, os

''' this class is used to generate items! '''
class Pickup:

    def __init__(self, img_name, x_pos, y_pos):

        # image used for item
        self.image = pygame.image.load(os.path.join("assets", img_name))

        # platform rect
        self.rect = self.image.get_rect()

        # rect positions
        self.rect.x = x_pos
        self.rect.y = y_pos

        # item collision
        self.item_collision = False