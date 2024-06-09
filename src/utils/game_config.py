class GameConfig:
    GAME_NAME = "FAHAD GAME"
    
    GUI_START_BTN = "START"
    GUI_OPTION_BTN = "OPTION"
    GUI_QUIT_BTN = "QUIT"
    
    # Define file paths and other global variables
    TILE_SET_PATH = "../assets/graphics/Dungeon_Tileset.png"
    PLAYER_SPRITESHEET_IDLE_PATH = "../assets/graphics/player/char_008_idle.png"
    PLAYER_SPRITESHEET_PATH = "../assets/graphics/player/Char_008.png"
    MAP_PATH = "../assets/maps/map.txt"
    TILE_SIZE = 32
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    PLAYER_START_POSITION = [100, 100]

    # Add other global settings as needed
    FPS = 60
    BACKGROUND_COLOR = (0, 0, 0)  # Black

# Example usage:
# print(GameConfig.SPRITESHEET_PATH)
# print(GameConfig.TILE_SIZE)