import pygame, os

# class to generate our sprite!
class Character(pygame.sprite.Sprite):

    # main
    def __init__(self, pos):
        super(Character, self).__init__()
        self.image = pygame.image.load(os.path.join("assets", "blue_alien.png"))
        self.rect = self.image.get_rect()
        self.rect.center = pos

    # method to move sprite right
    def move_right(self, pixels):
        self.rect.x += pixels

    # method to move sprite left
    def move_left(self, pixels):
        self.rect.x -= pixels

    