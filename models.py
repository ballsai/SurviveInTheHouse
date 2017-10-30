import arcade
import time
import random
MOVEMENT_SPEED = 5
CHAR_SCALE = 1

class Model():
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y 

class Object(arcade.Sprite):
    def __init__(self,world,x,y):
        super().__init__()
        self.world = world
        self.x = x
        self.y = y
        self.center_x = self.x
        self.center_y = self.y
 
class Player(arcade.Sprite):

    def __init__(self,world,x,y):
        super().__init__()
        self.world = world
        self.x = x
        self.y = y
        self.center_x = self.x
        self.center_y = self.y
        
        self.texture_left = []
        self.texture_left.append(arcade.load_texture("images/player/char_w01.png",scale =CHAR_SCALE))
        self.texture_left.append(arcade.load_texture("images/player/char_w02.png",scale =CHAR_SCALE))
        self.texture_left.append(arcade.load_texture("images/player/char_w03.png",scale =CHAR_SCALE))
        self.texture_left.append(arcade.load_texture("images/player/char_w04.png",scale =CHAR_SCALE))
        self.texture_left.append(arcade.load_texture("images/player/char_w05.png",scale =CHAR_SCALE))
        self.texture_left.append(arcade.load_texture("images/player/char_w06.png",scale =CHAR_SCALE))
        self.texture_left.append(arcade.load_texture("images/player/char_w07.png",scale =CHAR_SCALE))
        self.texture_left.append(arcade.load_texture("images/player/char_w08.png",scale =CHAR_SCALE))
        self.texture_left.append(arcade.load_texture("images/player/char_w09.png",scale =CHAR_SCALE))


        self.texture_right = []
        self.texture_right.append(arcade.load_texture("images/player/char_e01.png",scale =CHAR_SCALE))
        self.texture_right.append(arcade.load_texture("images/player/char_e02.png",scale =CHAR_SCALE))
        self.texture_right.append(arcade.load_texture("images/player/char_e03.png",scale =CHAR_SCALE))
        self.texture_right.append(arcade.load_texture("images/player/char_e04.png",scale =CHAR_SCALE))
        self.texture_right.append(arcade.load_texture("images/player/char_e05.png",scale =CHAR_SCALE))
        self.texture_right.append(arcade.load_texture("images/player/char_e06.png",scale =CHAR_SCALE))
        self.texture_right.append(arcade.load_texture("images/player/char_e07.png",scale =CHAR_SCALE))
        self.texture_right.append(arcade.load_texture("images/player/char_e08.png",scale =CHAR_SCALE))
        self.texture_right.append(arcade.load_texture("images/player/char_e09.png",scale =CHAR_SCALE))

        self.texture_down = []
        self.texture_down.append(arcade.load_texture("images/player/char_s01.png",scale =CHAR_SCALE))
        self.texture_down.append(arcade.load_texture("images/player/char_s02.png",scale =CHAR_SCALE))
        self.texture_down.append(arcade.load_texture("images/player/char_s03.png",scale =CHAR_SCALE))
        self.texture_down.append(arcade.load_texture("images/player/char_s04.png",scale =CHAR_SCALE))
        self.texture_down.append(arcade.load_texture("images/player/char_s05.png",scale =CHAR_SCALE))
        self.texture_down.append(arcade.load_texture("images/player/char_s06.png",scale =CHAR_SCALE))
        self.texture_down.append(arcade.load_texture("images/player/char_s07.png",scale =CHAR_SCALE))
        self.texture_down.append(arcade.load_texture("images/player/char_s08.png",scale =CHAR_SCALE))
        self.texture_down.append(arcade.load_texture("images/player/char_s09.png",scale =CHAR_SCALE))

        self.texture_up = []
        self.texture_up.append(arcade.load_texture("images/player/char_n01.png",scale =CHAR_SCALE))
        self.texture_up.append(arcade.load_texture("images/player/char_n02.png",scale =CHAR_SCALE))
        self.texture_up.append(arcade.load_texture("images/player/char_n03.png",scale =CHAR_SCALE))
        self.texture_up.append(arcade.load_texture("images/player/char_n04.png",scale =CHAR_SCALE))
        self.texture_up.append(arcade.load_texture("images/player/char_n05.png",scale =CHAR_SCALE))
        self.texture_up.append(arcade.load_texture("images/player/char_n06.png",scale =CHAR_SCALE))
        self.texture_up.append(arcade.load_texture("images/player/char_n07.png",scale =CHAR_SCALE))
        self.texture_up.append(arcade.load_texture("images/player/char_n08.png",scale =CHAR_SCALE))
        self.texture_up.append(arcade.load_texture("images/player/char_n09.png",scale =CHAR_SCALE))
        
        self.index = 0
        self.texture = self.texture_down[self.index]
    #################################################################
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.change_y = MOVEMENT_SPEED
            self.change_x = 0
        if key == arcade.key.DOWN:
            self.change_y = -MOVEMENT_SPEED
            self.change_x = 0
        if key == arcade.key.LEFT:
            self.change_x = -MOVEMENT_SPEED
            self.change_y = 0
        if key == arcade.key.RIGHT:
            self.change_x = MOVEMENT_SPEED
            self.change_y = 0
    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.change_x = 0
    #################################################################
    def hit_wall(self,wall,top_height,bottom_height,left_width,right_width):
        if ( self.left > wall.left-left_width and
             self.right < wall.right+right_width ):

            if (self.top > wall.bottom-bottom_height-1 and 
                self.top < wall.top ):
                self.top = wall.bottom-bottom_height-1

            if (self.bottom <wall.top+top_height+1 and
                self.top > wall.bottom):
                self.bottom = wall.top+top_height+1

        if (self.bottom < wall.top+top_height and 
            self.top > wall.bottom):

            if (self.left > wall.left-left_width-5 and
                self.left < wall.right):
                self.left = wall.right-left_width-5
            
            if (self.right < wall.right+right_width+5 and
                self.right > wall.left):
                self.right = wall.right+right_width+5

    ##################################################################
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        
        # Change image when sprite move ###########################################
        if self.change_x < 0:
            self.index += 1
            if self.index >= len(self.texture_left):
                self.index = 0
            self.texture = self.texture_left[self.index]
            
        elif self.change_x > 0:
            self.index += 1
            if self.index >= len(self.texture_right):
                self.index = 0
            self.texture = self.texture_right[self.index]
        
        elif self.change_y <0:
            self.index += 1
            if self.index >= len(self.texture_down):
                self.index = 0
            self.texture = self.texture_down[self.index]
            
        elif self.change_y >0:
            self.index += 1
            if self.index >= len(self.texture_up):
                self.index = 0
            self.texture = self.texture_up[self.index]
            
        ########################################################################
        self.hit_wall(wall=self.world.wall_1,top_height=44 ,
                        bottom_height=5,left_width=120,right_width=135)
        self.hit_wall(wall=self.world.wall_2,top_height=44 ,
                        bottom_height=5,left_width=60,right_width=60)
        self.hit_wall(wall=self.world.wall_3,top_height=44 ,
                        bottom_height=5,left_width=105,right_width=108)
        self.hit_wall(wall=self.world.wall_4,top_height=40 ,
                        bottom_height=5,left_width=90,right_width=62.5)
        self.hit_wall(wall=self.world.wall_5,top_height=44 ,
                        bottom_height=5,left_width=175,right_width=185)
        self.hit_wall(wall=self.world.wall_6,top_height=44 ,
                        bottom_height=5,left_width=185,right_width=175)
        self.hit_wall(wall=self.world.wall_7,top_height=70 ,
                        bottom_height=5,left_width=35,right_width=45)
        self.hit_wall(wall=self.world.wall_8,top_height=67.5 ,         
                        bottom_height=15,left_width=35,right_width=45)
        self.hit_wall(wall=self.world.wall_9,top_height=70,
                        bottom_height=5,left_width=35,right_width=45)
        self.hit_wall(wall=self.world.wall_10,top_height=67.5 ,
                        bottom_height=15,left_width=35,right_width=45)

        ########################################################################
        if self.left < 0:
            self.left = 1
                   
        if self.right > self.world.width-1:
            self.right = self.world.width-1
                   
        if self.bottom <0:
            self.bottom = 1
                    
        if self.top > self.world.height -1:
            self.top = self.world.height -1 
                   
        ########################################################################
class Ghost(arcade.Sprite):

    def __init__(self,world,x,y,speed):
        super().__init__()
        self.world = world
        self.x = x
        self.y = y
        self.center_x = self.x
        self.center_y = self.y
        self.speed = speed
        self.change_dir_time = 0
        
        self.texture_left = []
        self.texture_left.append(arcade.load_texture("images/characters/ghost_w01.png",scale =CHAR_SCALE))
        self.texture_left.append(arcade.load_texture("images/characters/ghost_w02.png",scale =CHAR_SCALE))
        self.texture_left.append(arcade.load_texture("images/characters/ghost_w03.png",scale =CHAR_SCALE))
        self.texture_left.append(arcade.load_texture("images/characters/ghost_w04.png",scale =CHAR_SCALE))
        self.texture_left.append(arcade.load_texture("images/characters/ghost_w05.png",scale =CHAR_SCALE))
        self.texture_left.append(arcade.load_texture("images/characters/ghost_w06.png",scale =CHAR_SCALE))
        self.texture_left.append(arcade.load_texture("images/characters/ghost_w07.png",scale =CHAR_SCALE))
        self.texture_left.append(arcade.load_texture("images/characters/ghost_w08.png",scale =CHAR_SCALE))
        self.texture_left.append(arcade.load_texture("images/characters/ghost_w09.png",scale =CHAR_SCALE))


        self.texture_right = []
        self.texture_right.append(arcade.load_texture("images/characters/ghost_e01.png",scale =CHAR_SCALE))
        self.texture_right.append(arcade.load_texture("images/characters/ghost_e02.png",scale =CHAR_SCALE))
        self.texture_right.append(arcade.load_texture("images/characters/ghost_e03.png",scale =CHAR_SCALE))
        self.texture_right.append(arcade.load_texture("images/characters/ghost_e04.png",scale =CHAR_SCALE))
        self.texture_right.append(arcade.load_texture("images/characters/ghost_e05.png",scale =CHAR_SCALE))
        self.texture_right.append(arcade.load_texture("images/characters/ghost_e06.png",scale =CHAR_SCALE))
        self.texture_right.append(arcade.load_texture("images/characters/ghost_e07.png",scale =CHAR_SCALE))
        self.texture_right.append(arcade.load_texture("images/characters/ghost_e08.png",scale =CHAR_SCALE))
        self.texture_right.append(arcade.load_texture("images/characters/ghost_e09.png",scale =CHAR_SCALE))

        self.texture_down = []
        self.texture_down.append(arcade.load_texture("images/characters/ghost_s01.png",scale =CHAR_SCALE))
        self.texture_down.append(arcade.load_texture("images/characters/ghost_s02.png",scale =CHAR_SCALE))
        self.texture_down.append(arcade.load_texture("images/characters/ghost_s03.png",scale =CHAR_SCALE))
        self.texture_down.append(arcade.load_texture("images/characters/ghost_s04.png",scale =CHAR_SCALE))
        self.texture_down.append(arcade.load_texture("images/characters/ghost_s05.png",scale =CHAR_SCALE))
        self.texture_down.append(arcade.load_texture("images/characters/ghost_s06.png",scale =CHAR_SCALE))
        self.texture_down.append(arcade.load_texture("images/characters/ghost_s07.png",scale =CHAR_SCALE))
        self.texture_down.append(arcade.load_texture("images/characters/ghost_s08.png",scale =CHAR_SCALE))
        self.texture_down.append(arcade.load_texture("images/characters/ghost_s09.png",scale =CHAR_SCALE))

        self.texture_up = []
        self.texture_up.append(arcade.load_texture("images/characters/ghost_n01.png",scale =CHAR_SCALE))
        self.texture_up.append(arcade.load_texture("images/characters/ghost_n02.png",scale =CHAR_SCALE))
        self.texture_up.append(arcade.load_texture("images/characters/ghost_n03.png",scale =CHAR_SCALE))
        self.texture_up.append(arcade.load_texture("images/characters/ghost_n04.png",scale =CHAR_SCALE))
        self.texture_up.append(arcade.load_texture("images/characters/ghost_n05.png",scale =CHAR_SCALE))
        self.texture_up.append(arcade.load_texture("images/characters/ghost_n06.png",scale =CHAR_SCALE))
        self.texture_up.append(arcade.load_texture("images/characters/ghost_n07.png",scale =CHAR_SCALE))
        self.texture_up.append(arcade.load_texture("images/characters/ghost_n08.png",scale =CHAR_SCALE))
        self.texture_up.append(arcade.load_texture("images/characters/ghost_n09.png",scale =CHAR_SCALE))
        
        self.index = 0
        self.texture = self.texture_down[self.index]

    def hit_wall(self,wall,top_height,bottom_height,left_width,right_width):
        if ( self.left > wall.left-left_width and
             self.right < wall.right+right_width ):

            if (self.top > wall.bottom-bottom_height-1 and 
                self.top < wall.top ):
                self.top = wall.bottom-bottom_height-1
                self.change_dir_time = 0

            if (self.bottom <wall.top+top_height+1 and
                self.top > wall.bottom):
                self.bottom = wall.top+top_height+1
                self.change_dir_time = 0

        if (self.bottom < wall.top+top_height and 
            self.top > wall.bottom):

            if (self.left > wall.left-left_width-5 and
                self.left < wall.right):
                self.left = wall.right-left_width-5
                self.change_dir_time = 0
            
            if (self.right < wall.right+right_width+5 and
                self.right > wall.left):
                self.right = wall.right+right_width+5
                self.change_dir_time = 0

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        
        # Change image when sprite move ###########################################
        if self.change_x < 0:
            self.index += 1
            if self.index >= len(self.texture_left):
                self.index = 0
            self.texture = self.texture_left[self.index]
            
        elif self.change_x > 0:
            self.index += 1
            if self.index >= len(self.texture_right):
                self.index = 0
            self.texture = self.texture_right[self.index]
  
        elif self.change_y <0:
            self.index += 1
            if self.index >= len(self.texture_down):
                self.index = 0
            self.texture = self.texture_down[self.index]
            
        elif self.change_y >0:
            self.index += 1
            if self.index >= len(self.texture_up):
                self.index = 0
            self.texture = self.texture_up[self.index]
        ########################################################################

        # Ghost follow player ##################################################
        if self.change_dir_time%100 == 0:
            self.change_dir_time+=1
            self.dir = random.randint(1,4)
        else:
            self.change_dir_time+=1
        
        if (abs(self.center_x-self.world.player.center_x) <=200 and  
            abs(self.center_y-self.world.player.center_y) <=150 ):
            if abs(self.center_x-self.world.player.center_x)  >= 5 :
                
                if self.center_x < self.world.player.center_x:
                    if self.world.player.change_x < 0 and self.change_x >0 :
                        self.change_x = -self.speed
                        self.change_y = 0
                    else:
                        self.change_x = self.speed
                        self.change_y =0

                elif self.center_x >= self.world.player.center_x:
                    self.change_x = -self.speed
                    self.change_y =0
            
            elif abs(self.center_y-self.world.player.center_y) >=5: 
                
                if self.center_y < self.world.player.center_y:
                    self.change_x = 0
                    self.change_y =self.speed
                elif self.center_y >= self.world.player.center_y:
                    self.change_x = 0
                    self.change_y =-self.speed
            else:
                self.change_x = 0
                self.change_y = 0
        #########################################################################    
        else:

            if self.dir == 1 :
                self.change_y = 0
                self.change_x = self.speed
                                
            if self.dir == 2 :
                self.change_y = 0
                self.change_x = -self.speed
                                
            if self.dir == 3 :
                self.change_x = 0
                self.change_y = self.speed
                                
            if self.dir == 4 :
                self.change_x = 0
                self.change_y = -self.speed
        #**************************************************************
        self.hit_wall(wall=self.world.wall_1,top_height=44 ,
                        bottom_height=5,left_width=120,right_width=135)
        self.hit_wall(wall=self.world.wall_2,top_height=44 ,
                        bottom_height=5,left_width=60,right_width=60)
        self.hit_wall(wall=self.world.wall_3,top_height=44 ,
                        bottom_height=5,left_width=105,right_width=108)
        self.hit_wall(wall=self.world.wall_4,top_height=40 ,
                        bottom_height=5,left_width=90,right_width=62.5)
        self.hit_wall(wall=self.world.wall_5,top_height=44 ,
                        bottom_height=5,left_width=175,right_width=185)
        self.hit_wall(wall=self.world.wall_6,top_height=44 ,
                        bottom_height=5,left_width=185,right_width=175)
        self.hit_wall(wall=self.world.wall_7,top_height=70 ,
                        bottom_height=5,left_width=35,right_width=35)
        self.hit_wall(wall=self.world.wall_8,top_height=67.5 ,         
                        bottom_height=15,left_width=35,right_width=35)
        self.hit_wall(wall=self.world.wall_9,top_height=70,
                        bottom_height=5,left_width=35,right_width=35)
        self.hit_wall(wall=self.world.wall_10,top_height=67.5 ,
                        bottom_height=15,left_width=35,right_width=35)
        if self.left < 0:
            self.left = 1
            self.change_dir_time = 0
        if self.right > self.world.width-1:
            self.right = self.world.width-1
            self.change_dir_time = 0      
        if self.bottom <0:
            self.bottom = 1
            self.change_dir_time = 0        
        if self.top > self.world.height -1:
            self.top = self.world.height -1 
            self.change_dir_time = 0 
 ########################################################################
class Bullet(arcade.Sprite):
    def update(self):
        self.center_y += BULLET_SPEED        
 ########################################################################
   
class World:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.total_time = 0
        self.release_ghost_time = 0
        self.release_bomb_time = 1
        self.release_food_time = 1
        self.count_ghost = 0
        self.start_game = True
        self.game_over = False
        self.count_down = 600
        self.energy = 100.0
        self.score = 0
        
        self.player_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.ghost_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.object_list = arcade.SpriteList()
        self.bomb_list = arcade.SpriteList()
        self.item_list = arcade.SpriteList()
        self.apple_list = arcade.SpriteList()
        self.food_list = arcade.SpriteList()
        
        
        self.player = Player(self,width//2,height//2)
        self.player_list.append(self.player)

        self.wall_1 = Object(self, 218//2,228)
        self.wall_2  = Object(self, 317.5,228)
        self.wall_3  = Object(self, 528,228)
        self.wall_4  = Object(self, 738,232)
        self.wall_5  = Object(self, 350//2,563)
        self.wall_6  = Object(self, 625,563)
        self.wall_7 = Object(self,345,326)
        self.wall_8 = Object(self,345,532.5)
        self.wall_9 = Object(self,345+110,326)
        self.wall_10 = Object(self,345+110,532.5)
        self.wall_list.append(self.wall_1)
        self.wall_list.append(self.wall_2)
        self.wall_list.append(self.wall_3)
        self.wall_list.append(self.wall_4)
        self.wall_list.append(self.wall_5)
        self.wall_list.append(self.wall_6)
        self.wall_list.append(self.wall_7)
        self.wall_list.append(self.wall_8)
        self.wall_list.append(self.wall_9)
        self.wall_list.append(self.wall_10)
       
    def on_key_press(self, key, modifiers):
        self.player.on_key_press(key, modifiers)

           
    def on_key_release(self, key, modifiers):
        self.player.on_key_release(key, modifiers)
        if key == arcade.key.ENTER:
            self.player.alpha = 1

    
    def update(self, delta):
        self.total_time += delta
        if self.start_game: 
            if not self.game_over:
        #set time to release ghost #############################################
                if self.release_ghost_time%300 == 0:
                    self.release_ghost_time += 1
                    for i in range(random.randint(1,2)):  
                        self.ghost_w = Ghost(self,0,random.randint(0,200),random.randint(1,4))
                        self.ghost_n = Ghost(self,random.randint(380,440),self.height,random.randint(1,4))
                        self.ghost_e = Ghost(self,self.width,random.randint(0,200),random.randint(1,4))
                    
                        self.ghost_list.append(self.ghost_w)
                        self.ghost_list.append(self.ghost_n)
                        self.ghost_list.append(self.ghost_e)
                else:
                    self.release_ghost_time += 1
                ########################################################################
                if self.release_bomb_time%400 == 0:
                    self.release_bomb_time += 1

                    bomb = arcade.Sprite("images/bomb.png",0.8)
                    bomb.center_x = random.randint(0,self.width)
                    bomb.center_y = random.randint(0,self.height)
                
                    if ( ( 10<bomb.center_x <self.width-10  and 10<bomb.center_y<220) or
                         ( 10<bomb.center_x <340 and 273<bomb.center_y<510 )          or 
                         ( 460<bomb.center_x<self.width-10 and 273<bomb.center_y<510) or   
                           360<bomb.center_x<440 and 0<bomb.center_y<self.height-20 ):                                                    
                        self.bomb_list.append(bomb)
                        self.item_list.append(bomb)

                else:
                    self.release_bomb_time +=1

                    if len(self.item_list) != 0:
                        if self.count_down >0 :
                            self.count_down -=1 
                        else: 
                            self.bomb_list[0].kill()
                            self.count_down = 600
                           
                    #########################################################################
                if self.release_food_time%100 == 0:
                    self.release_food_time += 1

                    apple = arcade.Sprite("images/apple.png",0.8)
                    apple.center_x = random.randint(0,self.width)
                    apple.center_y = random.randint(0,self.height)
                    if ( ( 10<apple.center_x <self.width-10  and 10<apple.center_y<220) or
                         ( 10<apple.center_x <340 and 273<apple.center_y<510 )          or 
                         ( 460<apple.center_x<self.width-10 and 273<apple.center_y<510) or   
                           360<apple.center_x<440 and 0<apple.center_y<self.height-20 ):   
                        self.apple_list.append(apple)
                        self.food_list.append(apple)
                else:
                    self.release_food_time +=1    
                    if len(self.food_list) != 0:
                        if self.count_down >0 :
                            self.count_down -=1 
                        else: 
                            self.apple_list[0].kill()
                            self.count_down = 600
                            
                    #########################################################################    
                    ##########################################################################
                check_collision = arcade.check_for_collision_with_list(self.player,self.ghost_list)
                if len(check_collision) > 0:
                            
                    for ghost in check_collision:
                        if (abs(self.player.center_x-ghost.center_x) <5 and
                            abs(self.player.center_y-ghost.center_y) <5):
                            ghost.kill()
                            if self.energy > 0.00:        
                                self.energy -= 10.00

                            elif self.energy <0.00:
                                self.energy = 0.00
                                self.game_over = True
                               
                elif self.player.change_x !=0 or self.player.change_y !=0:
                    if self.energy > 0.00:
                        self.energy -= 0.05
                    else:
                        self.energy = 0.00
                        self.game_over = True
                    ###############################################################################    
                drop_item = arcade.check_for_collision_with_list(self.player,self.bomb_list)
                if len(drop_item) > 0:
                    for bomb in drop_item:
                        bomb.kill()
                    for i in range(len(self.ghost_list)):
                        self.ghost_list[0].kill()
                        self.score += 1

                eat_apple = arcade.check_for_collision_with_list(self.player,self.apple_list)
                if len(eat_apple) > 0:
                    for apple in eat_apple:
                        apple.kill()
                        self.energy += 8

        
                ########################################################################
                self.player_list.update()
                self.ghost_list.update()
                self.item_list.update()
                self.food_list.update()

       
    
       


        
        
                
                

        
    