import pygame, os

''' this class is used to generate ground! '''
class Ground(pygame.sprite.Sprite):
    
    # main
    def __init__(self, position, image_name):
        super().__init__()

        self.image = pygame.image.load(os.path.join("assets", image_name))
        self.image_x = position[0]
        self.image_y = position[1]

    # method to render
    def render(self, screen):
        screen.blit(self.image, (self.image_x, self.image_y))