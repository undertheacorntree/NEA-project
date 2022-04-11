import pygame, os

''' this class is used to generate the player! '''
class Player(pygame.sprite.Sprite):

    # MAIN
    def __init__(self, img_name, x_vel, y_vel, x_pos, y_pos, max_jump):
        super().__init__()

        # image used for sprite
        self.image = pygame.image.load(os.path.join("assets", img_name))

        # sprite rect
        self.rect = self.image.get_rect()

        # rect positions
        self.rect.x = x_pos
        self.rect.y = y_pos

        # velocities
        self.x_vel = x_vel
        self.y_vel = y_vel

        # gravity and jumping
        self.falling = True
        self.max_jump = max_jump
    
    # MOVEMENT
    def move(self, keys_pressed, window, platform_a):

        # these are to verify the screen boundaries
        window_width = window.get_width()
        window_height = window.get_height()

        # MOVE LEFT
        # if the pressed key, the position of the sprite and the distance it will move
        # is less than the window width and the sprite width
        if keys_pressed[pygame.K_a] and self.rect.x - self.x_vel > 0:
                         
            # move the sprite to the left
            self.rect.x -= self.x_vel

        # MOVE RIGHT
        # if the pressed key, the position of the sprite and the distance it will move
        # is less than the window width and the sprite width
        if keys_pressed[pygame.K_d] and self.rect.x + self.x_vel < (window_width - self.rect.width):
          
            # move the sprite to the right
            self.rect.x += self.x_vel

        # JUMP
        # if [w] is pressed and not falling
        if keys_pressed[pygame.K_w] and self.falling == False:

            # increase the vertical position of the sprite on screen
            self.y_vel -= self.max_jump

            # change state to falling
            self.falling = True

        # GRAVITY
        if self.falling == True:

            # if the height, the fall, and the velocity increment are larger
            # than the lower boundary of the window height, plus the sprite height
            # stop the sprite from breaching the lower part of the screen
            if (self.rect.y + self.y_vel + 1) > (window_height - self.rect.height):
                
                # set the sprite onto the ground
                self.rect.y = window_height - self.rect.height

                # it is no longer falling
                self.falling = False

                # reset the velocity
                self.y_vel = 0

            else:
                # decrease the velocity
                self.y_vel += 1

                # change the vertical position of the sprite on screen
                self.rect.y += self.y_vel

                ######### half this later for slow fall speed, could be doubled for boots
        
        if self.rect.colliderect(platform_a):
            if platform_a.rect.top - self.rect.bottom == 0:
                self.y_vel *= -1
                print("ayo")