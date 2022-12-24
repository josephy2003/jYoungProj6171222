import arcade
from constants import *
from game_view import GameView
from guide import InstructionView

#window dimensions
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 1440
WINDOW_TITLE = 'MyGame'

#co-op sizing
PLAYER_SCALING = 2
TITLE_SCALING = 1
ENEMY_SCALING = 1



def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    'color' = arcade.set_background_color(arcade.color.BOSTON_UNIVERSITY_RED)
    start_view = guide()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()

