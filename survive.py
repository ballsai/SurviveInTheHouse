import arcade
from models import World,Player,Box,Ghost_LV1
from pyglet.window import key

 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
 
        super().__init__(*args, **kwargs)
 
    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
 
    def draw(self):
        self.sync_with_model()
        super().draw()

 
class SurviveWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
  
        
        self.world = World(width, height)
         
        self.player_sprite = ModelSprite("images/player.png",model=self.world.player) #1 self.player_sprite = arcade.Sprite("images/player.png",0.5)
        self.box_sprite = ModelSprite("images/box.png",model=self.world.box) #self.box_sprite = arcade.Sprite("images/box.png",0.2)
        self.ghost_sprite = ModelSprite("images/ghost_lv1.png",model=self.world.ghost_lv1)

        arcade.set_background_color(arcade.color.AMAZON)

    def on_key_press(self, key, modifiers): # checked keyboard : if keyboard pressed - print "key pressed"
       pass
    
    def on_draw(self):
        arcade.start_render()    
        self.world.control(keys)

        self.box_sprite.draw() 
        
        if self.world.player.y >= self.world.box.y+40:
            self.player_sprite.draw()
            self.box_sprite.draw()
        else:
             self.player_sprite.draw()

        if self.world.ghost_lv1.y >= self.world.box.y+40:
            self.ghost_sprite.draw()
            self.box_sprite.draw()
        else:
            self.ghost_sprite.draw()
        
        
    def update(self,delta):
        self.world.update(delta)

        
 
if __name__ == '__main__':
    window = SurviveWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    keys = key.KeyStateHandler()
    window.push_handlers(keys)
    

    arcade.run()