import pygame, os

''' this class is used to generate platforms! '''
class Podium:

    # MAIN
    def __init__(self, img_name, x_pos, y_pos):

        # image used for platform
        self.image = pygame.image.load(os.path.join("assets", img_name))

        # platform rect
        self.rect = self.image.get_rect()

        # rect positions
        self.rect.x = x_pos
        self.rect.y = y_pos

        # rect boundaries
        self.rect_top = self.rect.top
        self.rect_bottom = self.rect.bottom
        self.rect_right = self.rect.right
        self.rect_left = self.rect.left

    def get_rect_attribute_list(self):
        return [self.rect, self.rect_top, self.rect_bottom, self.rect_left, self.rect_right]