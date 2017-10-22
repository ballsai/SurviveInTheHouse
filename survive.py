import arcade
from random import randint
from models import World,Player,Box,Ghost
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
        arcade.set_background_color(arcade.color.AMAZON)
        self.timer_text = None
        self.box_sprite = ModelSprite("images/box.png",model=self.world.box)
      
      

    def on_key_press(self, key, modifiers): 
       self.world.on_key_press(key,modifiers)

    def on_key_release(self, key, modifiers):
       self.world.on_key_release(key,modifiers)
    
    
    def on_draw(self):
        arcade.start_render()    
        self.box_sprite.draw() 
        self.world.all_ghost_list.draw()

        if self.world.player.center_y >= self.world.box.y+40:
            self.world.all_player_list.draw()
            self.box_sprite.draw()
        else:
            self.world.all_player_list.draw()

        minutes = int(self.world.total_time) // 60
        seconds = int(self.world.total_time) % 60
        output = f"Time: {minutes:02d}:{seconds:02d}"
        if not self.timer_text or self.timer_text.text != output:
            self.timer_text = arcade.create_text(output, arcade.color.BLACK, 10)

        # Output the timer text.
        arcade.render_text(self.timer_text, 700, 560)

    def update(self,delta):
        self.world.update(delta)

if __name__ == '__main__':
    window = SurviveWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    arcade.run()