import pygame, os

''' this class is used to generate items! '''
class Pickup:

    def __init__(self, img_name, item_default, x_pos, y_pos):

        # image used for item
        self.image = pygame.image.load(os.path.join("assets", img_name))
        
        # platform rect
        self.rect = self.image.get_rect()

        # rect positions
        self.rect.x = x_pos
        self.rect.y = y_pos

        # item information
        self.ITEM_ID = img_name[:-4]
        self.item_collected = False
        self.item_selected = False
        self.item_default = item_default