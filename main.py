import arcade

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450
SCREEN_TITLE = "Its me Mariooo :D"
CHARACTER_SCALING = 0.5
TILE_SCALING = 0.5


class Mygame(arcade.Window):
    """
    Main application class.
    """
    
    def __init__(self) -> None:
        
        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        # Define first attributes
        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.
        self.wall_list = None
        self.player_list = None
        
        # Separate variable that holds the player sprite
        self.player_sprite = None

        # Set background color
        arcade.set_background_color([175, 249, 240])
        
    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        # Create the sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)

        # Set up the player, specifically placing it at these coordinates
        image_player_source = './img/small_mario_right.png'
        self.player_sprite = arcade.Sprite(image_player_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 96
        self.player_list.append(self.player_sprite)

        # Create the ground
        wall = arcade.Sprite('./img/floor.png', TILE_SCALING)
        wall.center_x = 500
        wall.center_y = 64
        self.wall_list.append(wall)

        # Create boxes
        coordinate_list_box = [[512, 96], [256,96], [768, 96]]

        for coordinate in coordinate_list_box:
            # Create boxes on the ground
            box = arcade.Sprite('./img/sbox.png',CHARACTER_SCALING)
            box.position = coordinate
            self.wall_list.append(box)
        
        # Create clouds
        coordinate_list_clouds = [[250, 300], [500, 300], [750, 300], [1000, 300]]
        
        for coordinates in coordinate_list_clouds:
            # Create clouds on the sky
            cloud = arcade.Sprite('./img/clouds.png',CHARACTER_SCALING)
            cloud.position = coordinates
            self.wall_list.append(cloud)
        
    def on_draw(self):
        """Render the screen."""
        
        # Clear the screen to the background color
        self.clear()
        
        # Code to draw the screen goes here
        # Draw our sprites
        self.wall_list.draw()
        self.player_list.draw()


def main():
    """ Main function """

    window = Mygame()
    window.setup()
    arcade.run()


if __name__ == '__main__':
    main()
