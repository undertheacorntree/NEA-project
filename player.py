import pygame, os

''' this class is used to generate the player! '''
class Player(pygame.sprite.Sprite):

    # MAIN
    def __init__(self, image_names, x_vel, y_vel, x_pos, y_pos, max_jump, player_weight):
        super().__init__()

        # image used for sprite
        self.image_name = image_names[0]
        self.image = pygame.image.load(os.path.join("assets", self.image_name))

        # sprite rect
        self.rect = self.image.get_rect()

        # rect positions
        self.rect.x = x_pos
        self.rect.y = y_pos

        # velocities
        self.DEFAULT_X_VEL = x_vel
        self.DEFAULT_Y_VEL = y_vel
        self.current_x_vel = x_vel
        self.current_y_vel = y_vel

        # weighting
        self.DEFAULT_PLAYER_WEIGHT = player_weight
        self.current_player_weight = player_weight

        # movement
        self.moving_left = False
        self.moving_right = False

        # gravity and jumping
        self.falling = True
        self.jumping = False
        self.DEFAULT_MAX_JUMP = max_jump
        self.current_max_jump = max_jump

        # platform info
        self.on_platform = False
        self.current_platform = None
    
    # MOVEMENT
    def move(self, WINDOW, MENU_X, MENU_Y, platforms, items_available, items_gained):

        # these are to verify the screen boundaries
        WINDOW_WIDTH = WINDOW.get_width()
        WINDOW_HEIGHT = WINDOW.get_height()

        # MOVE LEFT
        # if the pressed key, the position of the sprite and the distance it will move
        # is less than the window width and the sprite width
        if (self.moving_left == True) and (self.rect.x - self.current_x_vel > 0):

            # move the sprite to the left
            self.rect.x -= self.current_x_vel

            # check each platform
            for platform in platforms:

                # if a collision with a platform
                if self.rect.colliderect(platform.rect):           
                
                    # if platform right side position and player left side position are within collision (<10px) distance
                    if abs((platform.rect_right) - self.rect.left) < platform.current_collision_tolerance_x + self.rect.width:
                    
                        # then move back to previous position
                        self.rect.x += self.current_x_vel

                        # stop checking when platform found
                        break

        # MOVE RIGHT
        # if the pressed key, the position of the sprite and the distance it will move
        # is less than the window width and the sprite width
        if (self.moving_right == True) and (self.rect.x + self.current_x_vel < (WINDOW_WIDTH - self.rect.width)):
          
            # move the sprite to the right
            self.rect.x += self.current_x_vel

            # check each platform
            for platform in platforms:

                # if a collision with a platform
                if self.rect.colliderect(platform.rect):           
            
                    # if platform left side position and player right side position are within collision (<10px) distance
                    if abs((platform.rect_left) - self.rect.right) < platform.current_collision_tolerance_x:
                    
                        # then move back to previous position
                        self.rect.x -= self.current_x_vel
                        
                        # stop checking when platform found
                        break

        # JUMP
        # if [w] is pressed and not falling
        if (self.jumping == True) and (self.falling == False):

            # increase the vertical position of the sprite on screen
            self.current_y_vel -= self.current_max_jump

            # check each platform
            for platform in platforms:

                # if a collision with a platform
                if self.rect.colliderect(platform.rect):

                    # if top of player collides with bottom of platform
                    if abs(platform.rect_bottom - self.rect.top) < platform.current_collision_tolerance_y:
                    
                        # set player to jump only as high as other platform
                        self.rect.y = platform.rect_bottom + self.rect.height 

                        # stop checking when platform found
                        break

            # change state to falling
            self.falling = True
            self.jumping = False
            self.on_platform = False

        # GRAVITY
        if self.falling == True:

            # if the height, the fall, and the velocity increment are larger
            # than the lower boundary of the window height, plus the sprite height
            # stop the sprite from breaching the lower part of the screen
            if (self.rect.y + self.current_y_vel + self.current_player_weight) > (WINDOW_HEIGHT - self.rect.height):
                
                # set the sprite onto the ground
                self.rect.y = WINDOW_HEIGHT - self.rect.height

                # it is no longer falling
                self.falling = False

                # reset the velocity
                self.current_y_vel = 0

            else:
                # decrease the velocity
                self.current_y_vel += self.current_player_weight

                # change the vertical position of the sprite on screen
                self.rect.y += self.current_y_vel

                for platform in platforms:

                    # if a collision with a platform
                    if self.rect.colliderect(platform.rect):
                    
                        # if bottom of player collides with top of platform
                        if abs((platform.rect_top) - self.rect.bottom) < platform.current_collision_tolerance_y:
                        
                            # set player on platform and reset velocity
                            self.rect.y = platform.rect_top - self.rect.height
                            self.falling = False
                            self.current_y_vel = 0

                            # current platform checks relative x-position to activate gravity
                            self.on_platform = True
                            self.current_platform = platform

                            # stop checking when platform found
                            break

        # PLATFORM COLLISION VERIFICATION
        if self.on_platform == True:

            # if player outside of left/right boundaries
            if ((self.rect.right < self.current_platform.rect_left) or (self.rect.left > self.current_platform.rect_right)):
                    
                # re-introduce gravity
                self.on_platform = False
                self.falling = True

            # ITEM PICKUP
            for item in items_available:

                # if an item is picked up
                if self.rect.colliderect(item.rect):

                    # remove from avaliable items
                    items_available.remove(item)

                    # append at second position
                    items_gained.insert(1, item)

                    # set new positions
                    item.rect.x = MENU_X
                    item.rect.y = MENU_Y

                    # set the attributes
                    self.item_select(items_gained, platforms)

    # ITEM SELECTION
    def item_select(self, items_gained, platforms):
        
        # unselect first item
        items_gained[0].item_selected = False

        # add it to the end of the list
        items_gained.append(items_gained[0])

        # remove first item
        items_gained.remove(items_gained[0])

        # select new first item
        items_gained[0].item_selected = True        
    
        # ADD ATTRIBUTES
        # no item attributes
        if items_gained[0].ITEM_ID == 'no_item':
            self.current_player_weight = self.DEFAULT_PLAYER_WEIGHT
            self.current_x_vel = self.DEFAULT_X_VEL
            self.current_y_vel = self.DEFAULT_Y_VEL
            self.current_max_jump = self.DEFAULT_MAX_JUMP

        # heavy boots attributes
        if items_gained[0].ITEM_ID == 'heavy_boots':
            self.current_player_weight = self.DEFAULT_PLAYER_WEIGHT * 0.5
            self.current_x_vel = self.DEFAULT_X_VEL * self.current_player_weight
            self.current_y_vel = self.DEFAULT_Y_VEL * self.current_player_weight
            self.current_max_jump = 0

        # speedy boots attributes
        if items_gained[0].ITEM_ID == 'speedy_boots':
            self.current_player_weight = self.DEFAULT_PLAYER_WEIGHT * 1.5
            self.current_x_vel = self.DEFAULT_X_VEL * self.current_player_weight
            self.current_y_vel = self.DEFAULT_Y_VEL * self.current_player_weight
            self.current_max_jump = self.DEFAULT_MAX_JUMP
                    
        # exploding flower attributes
        if items_gained[0].ITEM_ID == 'exploding_flower':
            self.current_player_weight = self.DEFAULT_PLAYER_WEIGHT
            self.current_x_vel = self.DEFAULT_X_VEL
            self.current_y_vel = self.DEFAULT_Y_VEL
            self.current_max_jump = self.DEFAULT_MAX_JUMP

        # change col tol for SPEED
        for platform in platforms:
            platform.current_collision_tolerance_x = platform.DEFAULT_COLLISION_TOLERANCE_X * (self.current_player_weight)
            platform.current_collision_tolerance_y = platform.DEFAULT_COLLISION_TOLERANCE_Y * (self.current_player_weight)