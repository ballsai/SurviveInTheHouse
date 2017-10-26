import arcade
from random import randint
from models import World,Player,Object,Ghost
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
        arcade.set_background_color(arcade.color.DARK_SLATE_GRAY)
        self.timer_text = None
        self.background = arcade.load_texture("images/background.png")
        
        self.wall_1 = ModelSprite("images/wall_01.png",model=self.world.wall_1)
        self.wall_2 = ModelSprite("images/wall_02.png",model=self.world.wall_2)
        self.wall_3 = ModelSprite("images/wall_03.png",model=self.world.wall_3)
        self.wall_4 = ModelSprite("images/wall_04.png",model=self.world.wall_4)
        self.wall_5 = ModelSprite("images/wall_05.png",model=self.world.wall_5)
        self.wall_6 = ModelSprite("images/wall_06.png",model=self.world.wall_6)
        self.wall_7 = ModelSprite("images/wall_09.png",model=self.world.wall_7)
        self.wall_8 = ModelSprite("images/wall_10.png",model=self.world.wall_8)
        self.wall_9 = ModelSprite("images/wall_09.png",model=self.world.wall_9)
        
        self.wall_10 = ModelSprite("images/wall_10.png",model=self.world.wall_10)
        self.box = ModelSprite("images/box.png",model=self.world.box)

        

    def on_key_press(self, key, modifiers): 
       self.world.on_key_press(key,modifiers)

    def on_key_release(self, key, modifiers):
       self.world.on_key_release(key,modifiers)
    
    
    def on_draw(self):
        arcade.start_render()    

        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
       
        self.box.draw()
        self.wall_1.draw()
        self.wall_7.draw()
        self.wall_2.draw()
        self.wall_9.draw()
        self.wall_3.draw()
        self.wall_4.draw()
        self.wall_5.draw()
        self.wall_6.draw()
        self.wall_8.draw()
        self.wall_10.draw()
        #self.world.ghost_list.draw()
        self.world.player_list.draw()
       
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