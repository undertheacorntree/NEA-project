import pygame, os

# class to generate our character!
class Character(pygame.sprite.Sprite):

    def __init__(self, pos):
        super(Character, self).__init__()
        self.image = pygame.image.load(os.path.join('assets', 'blue_alien.png'))
        self.rect = self.image.get_rect()
        self.rect.center = pos