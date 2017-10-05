import arcade
from pyglet.window import key

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
            self.y += 5
        elif keys[key.DOWN]:
            self.y -= 5
        elif keys[key.LEFT]:
            self.x -= 5
        elif keys[key.RIGHT]:
            self.x += 5
    

    def update(self, delta):
        if self.x < 0:
            self.x = 0


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

        if self.player.hit(self.box, 200):
           self.player.x -= 5 
           self.player.y -= 5



      
        

        



   
           
  
    
        