import pygame, os

''' this class is used to generate sprites! '''
class Character(pygame.sprite.Sprite):

    # main
    def __init__(self, position, image_name):
        super().__init__()
        self.image = pygame.image.load(os.path.join("assets", image_name))
        self.rect = self.image.get_rect()
        self.rect.center = position

    # method to move sprite right
    def move_right(self, pixels):
        self.rect.x += pixels

    # method to move sprite left
    def move_left(self, pixels):
        self.rect.x -= pixels