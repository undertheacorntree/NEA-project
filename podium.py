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

        # adds a tolerance for additional pixels
        # higher col tol to account for to change in (falling) y-velocity
        self.DEFAULT_COLLISION_TOLERANCE_X = 10
        self.DEFAULT_COLLISION_TOLERANCE_Y = 20        
        self.current_collision_tolerance_x = self.DEFAULT_COLLISION_TOLERANCE_X
        self.current_collision_tolerance_y = self.DEFAULT_COLLISION_TOLERANCE_Y