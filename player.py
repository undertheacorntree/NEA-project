import pygame, os

''' this class is used to generate the player! '''
class Player(pygame.sprite.Sprite):

    # MAIN
    def __init__(self, img_name, x_vel, y_vel, x_pos, y_pos, max_jump):
        super().__init__()

        # image used for sprite
        self.image_name = img_name
        self.image = pygame.image.load(os.path.join("assets", self.image_name))

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

        # platform info
        self.on_platform = False
        self.current_platform = None
    
    # MOVEMENT
    def move(self, keys_pressed, window, platforms, items):

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

            # check each platform
            for platform in platforms:

                # if a collision with a platform
                if self.rect.colliderect(getattr(platform, 'rect')):           
                
                    # if platform right side position and player left side position are within collision (<10px) distance
                    if abs(getattr(platform, 'rect_right') - self.rect.left) < COLLISION_TOLERANCE_X + self.rect.width:
                    
                        # then move back to previous position
                        self.rect.x += self.x_vel

                        # stop checking when platform found
                        break

        # MOVE RIGHT
        # if the pressed key, the position of the sprite and the distance it will move
        # is less than the window width and the sprite width
        if keys_pressed[pygame.K_d] and self.rect.x + self.x_vel < (window_width - self.rect.width):
          
            # move the sprite to the right
            self.rect.x += self.x_vel

            # check each platform
            for platform in platforms:

                # if a collision with a platform
                if self.rect.colliderect(getattr(platform, 'rect')):           
            
                    # if platform left side position and player right side position are within collision (<10px) distance
                    if abs(getattr(platform, 'rect_left') - self.rect.right) < COLLISION_TOLERANCE_X:
                    
                        # then move back to previous position
                        self.rect.x -= self.x_vel
                        
                        # stop checking when platform found
                        break

        # JUMP
        # if [w] is pressed and not falling
        if (keys_pressed[pygame.K_w]) and (self.falling == False):

            # increase the vertical position of the sprite on screen
            self.y_vel -= self.max_jump

            # check each platform
            for platform in platforms:

                # if a collision with a platform
                if self.rect.colliderect(getattr(platform, 'rect')):

                    # if top of player collides with bottom of platform
                    if abs(getattr(platform, 'rect_bottom') - self.rect.top) < COLLISION_TOLERANCE_Y:
                    
                        # set player to jump only as high as other platform
                        self.rect.y = getattr(platform, 'rect_bottom') + self.rect.height 

                        # stop checking when platform found
                        break

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

                for platform in platforms:

                    # if a collision with a platform
                    if self.rect.colliderect(getattr(platform, 'rect')):
                    
                        # if bottom of player collides with top of platform
                        if abs(getattr(platform, 'rect_top') - self.rect.bottom) < COLLISION_TOLERANCE_Y:
                        
                            # set player on platform and reset velocity
                            self.rect.y = getattr(platform, 'rect_top') - self.rect.height
                            self.falling = False
                            self.y_vel = 0

                            # current platform checks relative x-position to activate gravity
                            self.on_platform = True
                            self.current_platform = platform

                            # stop checking when platform found
                            break

        # PLATFORM COLLISION VERIFICATION
        if self.on_platform == True:

            # if player outside of left/right boundaries
            if (self.rect.right < getattr(self.current_platform, 'rect_left')) or (self.rect.left > getattr(self.current_platform, 'rect_right')):
                    
                # re-introduce gravity
                self.on_platform = False
                self.falling = True

            # ITEM PICKUP
            for item in items:
                if self.rect.colliderect(getattr(item, 'rect')):
                    setattr(item, 'item_collected', True)