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
        self.item_default = item_default
        self.item_selected = False

        # sets values upon pickup (True)
        self.item_set_default = False

        # sets default item to selected
        if self.item_default == True:
            self.item_selected = True