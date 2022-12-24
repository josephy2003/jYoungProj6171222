import arcade
import game_view


class guide(arcade.View):

    def on_show(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.BLACK)

        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):

        arcade.start_render()
        arcade.draw_text("SHIPS", self.window.width / 2, self.window.height / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Click to Start", self.window.width / 2, self.window.height / 2-75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        my_game_view = game_view.GameView()
        my_game_view.setup()
        self.window.show_view(my_game_view)
