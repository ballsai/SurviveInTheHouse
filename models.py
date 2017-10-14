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


class Player(Model):

    def __init__(self, world, x,y):
        super().__init__(world, x, y)

    def control(self, keys):
        if keys[key.UP]:
            self.y += MOVEMENT_SPEED
        elif keys[key.DOWN]:
            self.y -= MOVEMENT_SPEED
        elif keys[key.LEFT]:
            self.x -= MOVEMENT_SPEED
        elif keys[key.RIGHT]:
            self.x += MOVEMENT_SPEED
    

    def update(self, delta):
        
        if self.x < PLAYER_MARGIN:
            self.x += MOVEMENT_SPEED
        elif self.x > self.world.width-PLAYER_MARGIN:
            self.x -= MOVEMENT_SPEED
            
        elif self.y<PLAYER_MARGIN+30:
            self.y += MOVEMENT_SPEED 
        elif self.y >self.world.height-PLAYER_MARGIN-30:
            self.y -= MOVEMENT_SPEED 


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

    def update(self, delta):

        if abs(self.x-self.world.player.x) >= 1:
            
            if self.x < self.world.player.x:
                self.x += 1
            elif self.x > self.world.player.x:
                self.x -= 1

        elif abs(self.y-self.world.player.y) >= 1:
            if self.y < self.world.player.y:
                self.y += 1
            elif self.y > self.world.player.y:
                self.y -= 1
          


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.player = Player(self, 100,200)
        self.box = Box(self, 300,400)
        self.ghost_lv1 = Ghost_LV1(self,50,50)


    def control(self, keys):
        self.player.control(keys)
        if keys[key.SPACE]:
           print("SPACE")
        


    def update(self, delta):
        self.player.update(delta)
        self.ghost_lv1.update(delta)

        
        if self.player.hit_obj(self.box,0,40,-60,60):

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
                self.ghost_lv1.y += 1






                

      

      


            

        


       



      
        

        



   
           
  
    
        