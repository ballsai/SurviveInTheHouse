import arcade
from pyglet.window import key

MOVEMENT_SPEED = 5

class Model:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y 

    def hit(self, other, hit_size):
        return (abs(self.x - other.x) <= hit_size) and (abs(self.y - other.y) <= hit_size)

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
        #print(self.x,self.y)
        if self.x < 37:
            self.x += MOVEMENT_SPEED
        elif self.x > self.world.width-37:
            self.x -= MOVEMENT_SPEED
            print("Touch Edge")
        elif self.y<90:
            self.y += MOVEMENT_SPEED 
        elif self.y >self.world.height-90:
            self.y -= MOVEMENT_SPEED 


class Box(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y)
 
    def update(self, delta):
        if self.x < 37:
            self.x += self.player.x+100
        


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.player = Player(self, 100,100)
        self.box = Box(self, 300,400)


    def control(self, keys):
        self.player.control(keys)
        if keys[key.SPACE]:
           print("SPACE")
        


    def update(self, delta):
        self.player.update(delta)

        if self.player.hit(self.box, 100):

            self.box.x = self.player.x-100

        


       



      
        

        



   
           
  
    
        