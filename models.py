import arcade
from pyglet.window import key

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
            self.y += 5
        elif keys[key.DOWN]:
            self.y -= 5
        elif keys[key.LEFT]:
            self.x -= 5
        elif keys[key.RIGHT]:
            self.x += 5
    

    def update(self, delta):
        print(self.x,self.y)
        if self.x < 37:
            self.x += 5
        elif self.x > self.world.width-37:
            self.x -= 5
        elif self.y<90:
            self.y += 5
        elif self.y >self.world.height-90:
            self.y -= 5


class Box(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y)
 
    def update(self, delta):
        if self.y > 600:
            self.y -= 10


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.player = Player(self, 100,100)
        self.box = Box(self, 300,400)

    def control(self, keys):
        self.player.control(keys)


    def update(self, delta):
        self.player.update(delta)

       



      
        

        



   
           
  
    
        