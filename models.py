import arcade
from pyglet.window import key

PLAYER_MARGIN = 20
BOX_MARGIN = 40
MOVEMENT_SPEED = 2


class Model:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y 

    def hit_obj(self, obj, obj_bottom, obj_top, obj_left, obj_right):
        
        return (  self.y >= obj.y+obj_bottom  and 
                  self.y <= obj.y+obj_top     and 
                  self.x >= obj.x+obj_left    and 
                  self.x<= obj.x+obj_right  )


class Player(arcade.Sprite):

    def __init__(self):
        super().__init__()


        self.texture_left = []
        self.texture_left.append(arcade.load_texture("images/player/char_w01.png",scale =2))
        self.texture_left.append(arcade.load_texture("images/player/char_w02.png",scale =2))
        self.texture_left.append(arcade.load_texture("images/player/char_w03.png",scale =2))
        self.texture_left.append(arcade.load_texture("images/player/char_w04.png",scale =2))
        self.texture_left.append(arcade.load_texture("images/player/char_w05.png",scale =2))
        self.texture_left.append(arcade.load_texture("images/player/char_w06.png",scale =2))
        self.texture_left.append(arcade.load_texture("images/player/char_w07.png",scale =2))
        self.texture_left.append(arcade.load_texture("images/player/char_w08.png",scale =2))
        self.texture_left.append(arcade.load_texture("images/player/char_w09.png",scale =2))

        self.texture_right = []
        self.texture_right.append(arcade.load_texture("images/player/char_e01.png",scale =2))
        self.texture_right.append(arcade.load_texture("images/player/char_e02.png",scale =2))
        self.texture_right.append(arcade.load_texture("images/player/char_e03.png",scale =2))
        self.texture_right.append(arcade.load_texture("images/player/char_e04.png",scale =2))
        self.texture_right.append(arcade.load_texture("images/player/char_e05.png",scale =2))
        self.texture_right.append(arcade.load_texture("images/player/char_e06.png",scale =2))
        self.texture_right.append(arcade.load_texture("images/player/char_e07.png",scale =2))
        self.texture_right.append(arcade.load_texture("images/player/char_e08.png",scale =2))
        self.texture_right.append(arcade.load_texture("images/player/char_e09.png",scale =2))

        self.texture_down = []
        self.texture_down.append(arcade.load_texture("images/player/char_s01.png",scale =2))
        self.texture_down.append(arcade.load_texture("images/player/char_s02.png",scale =2))
        self.texture_down.append(arcade.load_texture("images/player/char_s03.png",scale =2))
        self.texture_down.append(arcade.load_texture("images/player/char_s04.png",scale =2))
        self.texture_down.append(arcade.load_texture("images/player/char_s05.png",scale =2))
        self.texture_down.append(arcade.load_texture("images/player/char_s06.png",scale =2))
        self.texture_down.append(arcade.load_texture("images/player/char_s07.png",scale =2))
        self.texture_down.append(arcade.load_texture("images/player/char_s08.png",scale =2))
        self.texture_down.append(arcade.load_texture("images/player/char_s09.png",scale =2))

        self.texture_up = []
        self.texture_up.append(arcade.load_texture("images/player/char_n01.png",scale =2))
        self.texture_up.append(arcade.load_texture("images/player/char_n02.png",scale =2))
        self.texture_up.append(arcade.load_texture("images/player/char_n03.png",scale =2))
        self.texture_up.append(arcade.load_texture("images/player/char_n04.png",scale =2))
        self.texture_up.append(arcade.load_texture("images/player/char_n05.png",scale =2))
        self.texture_up.append(arcade.load_texture("images/player/char_n06.png",scale =2))
        self.texture_up.append(arcade.load_texture("images/player/char_n07.png",scale =2))
        self.texture_up.append(arcade.load_texture("images/player/char_n08.png",scale =2))
        self.texture_up.append(arcade.load_texture("images/player/char_n09.png",scale =2))
        
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

        if self.left < 0:
            self.left = 0
        elif self.right > 800 - 1:
            self.right = 600 - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > 800 - 1:
            self.top = 600 - 1



class Box(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y)
 
    def update(self, delta):
        if self.x < 100:
            self.x += MOVEMENT_SPEED
        elif self.x > self.world.width-100:
            self.x -= MOVEMENT_SPEED
        elif self.y<100:
            self.y += MOVEMENT_SPEED 
        elif self.y >self.world.height-100:
            self.y -= MOVEMENT_SPEED 

class Ghost_LV1(Model):
    
   
    def __init__(self, world, x, y):
        super().__init__(world, x, y)
        self.count_time = 0

    def update(self, delta):
        
    
        pass

      
class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.player = Player()
        self.player.center_x = self.width//2
        self.player.center_y = self.height//2

        self.box = Box(self, 300,400)
        self.ghost_lv1 = Ghost_LV1(self,50,50)


    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
       
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0
        
        
    def update(self, delta):
        self.player.update()
        self.ghost_lv1.update(delta)
        
        
        '''if self.player.hit_obj(self.box,0,40,-60,60):

            if self.player.x == self.box.x-60:
                self.player.x -= MOVEMENT_SPEED
            elif self.player.x == self.box.x+60:
                self.player.x += MOVEMENT_SPEED
            elif self.player.y ==self.box.y:
                self.player.y -= MOVEMENT_SPEED
            elif self.player.y == self.box.y+40:
                self.player.y += MOVEMENT_SPEED

        if self.ghost_lv1.hit_obj(self.box,0,40,-60,60):

            if self.ghost_lv1.x == self.box.x-60:
                self.ghost_lv1.x -= 1
            elif self.ghost_lv1.x == self.box.x+60:
                self.ghost_lv1.x += 1
            elif self.ghost_lv1.y ==self.box.y:
                self.ghost_lv1.y -= 1
            elif self.ghost_lv1.y == self.box.y+40:
                self.ghost_lv1.y += 1'''

        


                
             
                
           

        
        
        


                

      

      


            

        


       



      
        

        



   
           
  
    
        