import pygame, os

# class to generate ground!
class Ground(pygame.sprite.Sprite):
    
    # main
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(os.path.join("assets", "test_ground_asset.png"))
        self.rect = self.image.get_rect()
        self.rect.center = pos

    # render method
    def render(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
