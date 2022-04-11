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
        self.on_platform = False
        self.max_jump = max_jump
    
    # MOVEMENT
    def move(self, keys_pressed, window, platforms, platform_a_rect, platform_a_rect_top, platform_a_rect_bottom, platform_a_rect_right, platform_a_rect_left):

        # these are to verify the screen boundaries
        window_width = window.get_width()
        window_height = window.get_height()

        # adds a tolerance for additional pixels
        # higher col tol to account for to change in (falling) y-velocity
        COLLISION_TOLERANCE_X = 10
        COLLISION_TOLERANCE_Y = 20

        # MOVE LEFT
        # if the pressed key, the position of the sprite and the distance it will move
        # is less than the window width and the sprite width
        if keys_pressed[pygame.K_a] and self.rect.x - self.x_vel > 0:
                         
            # move the sprite to the left
            self.rect.x -= self.x_vel

            # if a collision with a platform
            if self.rect.colliderect(platform_a_rect):           
                
                # if platform right side position and player left side position are within collision (<10px) distance
                if abs(platform_a_rect_right - self.rect.left) < COLLISION_TOLERANCE_X + self.rect.width:
                    
                    # then move back to previous position
                    self.rect.x += self.x_vel

        # MOVE RIGHT
        # if the pressed key, the position of the sprite and the distance it will move
        # is less than the window width and the sprite width
        if keys_pressed[pygame.K_d] and self.rect.x + self.x_vel < (window_width - self.rect.width):
          
            # move the sprite to the right
            self.rect.x += self.x_vel

            # if a collision with a platform
            if self.rect.colliderect(platform_a_rect):           
            
                # if platform left side position and player right side position are within collision (<10px) distance
                if abs(platform_a_rect_left - self.rect.right) < COLLISION_TOLERANCE_X:
                    
                    # then move back to previous position
                    self.rect.x -= self.x_vel

        # JUMP
        # if [w] is pressed and not falling
        if keys_pressed[pygame.K_w] and self.falling == False:

            # increase the vertical position of the sprite on screen
            self.y_vel -= self.max_jump

            # if a collision with a platform
            if self.rect.colliderect(platform_a_rect):

                # if top of player collides with bottom of platform
                if abs(platform_a_rect_bottom - self.rect.top) < COLLISION_TOLERANCE_Y:
                    
                    # set player to jump only as high as other platform
                    self.rect.y = platform_a_rect_bottom + self.rect.height 

            # change state to falling
            self.falling = True
            self.on_platform = False

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

                # if a collision with a platform
                if self.rect.colliderect(platform_a_rect):
                    
                    # if bottom of player collides with top of platform
                    if abs(platform_a_rect_top - self.rect.bottom) < COLLISION_TOLERANCE_Y:
                        
                        # set player on platform and reset velocity
                        self.rect.y = platform_a_rect_top - self.rect.height
                        self.falling = False
                        self.on_platform = True
                        self.y_vel = 0
        
        # PLATFORM COLLISION VERIFICATION
        if self.on_platform == True:

            # if player outside of left/right boundaries
            if (self.rect.right < platform_a_rect_left) or (self.rect.left > platform_a_rect_right):
                
                # re-introduce gravity
                self.on_platform = False
                self.falling = True