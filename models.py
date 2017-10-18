import arcade
import time
import random
from pyglet.window import key

PLAYER_MARGIN = 20
BOX_MARGIN = 40
MOVEMENT_SPEED = 5
CHAR_SCALE = 1.5
COUNT_GHOST = 10

class Model:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y 

    def hit_obj(self, obj, obj_bottom, obj_top, obj_left, obj_right):
        
        return (  self.center_y >= obj.y+obj_bottom  and 
                  self.center_y <= obj.y+obj_top     and 
                  self.center_x >= obj.x+obj_left    and 
                  self.center_x<= obj.x+obj_right  )


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
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.A:
            self.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.change_x = MOVEMENT_SPEED

        
    def on_key_release(self, key, modifiers):
       
        if key == arcade.key.W or key == arcade.key.S:
            self.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.change_x = 0

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        
       
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
            
        
        if self.left < 0:
            self.left = 0
        elif self.right > 800 - 1:
            self.right = 800 - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > 600 - 1:
            self.top = 600 - 1

class Ghost(arcade.Sprite):

    def __init__(self,world,x,y,delay):
        super().__init__()
        self.world = world
        self.x = x
        self.y = y
        self.delay = delay
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
    

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        
       
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

        if abs(self.center_x-self.world.player.center_x)  >= 10 :
            
            if self.center_x < self.world.player.center_x:
                self.change_x = MOVEMENT_SPEED-self.delay
                self.change_y =0
            elif self.center_x >= self.world.player.center_x:
                self.change_x = -MOVEMENT_SPEED+self.delay
        
                self.change_y = 0
        
        elif abs(self.center_y-self.world.player.center_y) >=20: 
            
            if self.center_y < self.world.player.center_y:
               self.change_y = MOVEMENT_SPEED-self.delay
               self.change_x = 0
            elif self.center_y >= self.world.player.center_y:
                self.change_y = -MOVEMENT_SPEED+self.delay
                self.change_x = 0
        else:
            self.change_x = 0
            self.change_y = 0

class Box(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y)
 
    def update(self, delta):
        pass
      
class World:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        arcade.set_background_color(arcade.color.AMAZON)
        self.total_time = 0.0
        self.all_player_list = arcade.SpriteList()
        self.all_ghost_list = arcade.SpriteList()
        
        self.player = Player(self,width//2,height//2)
        self.all_player_list.append(self.player)
        
        for i in range(COUNT_GHOST):
            self.ghost = Ghost(self,random.randrange(100)+i*(100),random.randrange(100)+i*(100),random.randrange(1,4))
            self.all_ghost_list.append(self.ghost)
        
        self.box = Box(self, 300,400)
        

    def on_key_press(self, key, modifiers):
        self.player.on_key_press(key, modifiers)
        if key == arcade.key.SPACE:
            for i in range(len(self.all_ghost_list)):
               self.all_ghost_list[i-(COUNT_GHOST-1)].kill()
               print(i)
               
                    
                
                
    def on_key_release(self, key, modifiers):
        self.player.on_key_release(key, modifiers)
        
        
    def update(self, delta):
        self.total_time += delta

        self.all_player_list.update()
        self.all_ghost_list.update()


    