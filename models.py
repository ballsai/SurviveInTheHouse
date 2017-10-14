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
        


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.player = Player(self, 100,200)
        self.box = Box(self, 300,400)


    def control(self, keys):
        self.player.control(keys)
        if keys[key.SPACE]:
           print("SPACE")
        


    def update(self, delta):
        self.player.update(delta)

        if self.player.y >= self.box.y and self.player.y <= self.box.y+40 and self.player.x+20 >= self.box.x-40 and self.player.x-20 <= self.box.x+40:
            if self.player.x+20 == self.box.x-40:
                self.player.x -= MOVEMENT_SPEED
            elif self.player.x-20 == self.box.x+40:
                self.player.x += MOVEMENT_SPEED
            elif self.player.y ==self.box.y:
                self.player.y -= MOVEMENT_SPEED
            elif self.player.y == self.box.y+40:
                self.player.y += MOVEMENT_SPEED






                

      

      


            

        


       



      
        

        



   
           
  
    
        