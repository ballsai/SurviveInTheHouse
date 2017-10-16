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
        
        self.all_sprites_list = arcade.SpriteList()
        
        self.player_sprite = self.world.player
        
        self.all_sprites_list.append(self.player_sprite)
        
        
        arcade.set_background_color(arcade.color.AMAZON)

    def on_key_press(self, key, modifiers): 
       self.world.on_key_press(key,modifiers)

    def on_key_release(self, key, modifiers):
       self.world.on_key_release(key,modifiers)
    
    
    def on_draw(self):
        arcade.start_render()    
        #self.box_sprite.draw() 
        self.all_sprites_list.draw()
        
    

    def update(self,delta):
        self.world.update(delta)
        self.all_sprites_list.update()
        
        
        
 
if __name__ == '__main__':
    window = SurviveWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    keys = key.KeyStateHandler()
    window.push_handlers(keys)
    

    arcade.run()