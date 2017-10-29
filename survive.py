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
        self.score_text = None
        self.energy_text = None
        
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
      
        

    def on_key_press(self, key, modifiers): 
       self.world.on_key_press(key,modifiers)

    def on_key_release(self, key, modifiers):
       self.world.on_key_release(key,modifiers)
    
    
    def on_draw(self):
        arcade.start_render()    

        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
       
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
        
        self.world.ghost_list.draw()
        self.world.player_list.draw()
        self.world.item_list.draw()
        self.world.food_list.draw()
       
       
      #######################################################
        output = f"Score: {self.world.score}"
        if not self.score_text or output != self.score_text.text:
            self.score_text = arcade.create_text(output, arcade.color.WHITE, 14)
        arcade.render_text(self.score_text, 10, 20)
        #######################################################
        output = f"Energy: {self.world.energy} %"
        if not self.energy_text or output != self.energy_text.text:
            self.energy_text = arcade.create_text(output, arcade.color.WHITE, 14)
        arcade.render_text(self.energy_text, 140, 20)

        if self.world.game_over:
            arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
            output = f"Your Score: {self.world.score}"
            if not self.score_text or output != self.score_text.text:
                self.score_text = arcade.create_text(output, arcade.color.WHITE, 30)
            arcade.render_text(self.score_text, 300, 300)
        if not self.world.start_game:
            arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

    def update(self,delta):
        self.world.update(delta)
        
        

if __name__ == '__main__':
    window = SurviveWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    arcade.run()