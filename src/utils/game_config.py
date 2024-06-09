class GameConfig:
    GAME_NAME = "FAHAD GAME"
    
    GUI_START_BTN = "START"
    GUI_OPTION_BTN = "OPTION"
    GUI_QUIT_BTN = "QUIT"
    
    # Define file paths and other global variables
    TILE_SET_PATH = "../assets/graphics/Dungeon_Tileset.png"
    PLAYER_SPRITESHEET_IDLE_PATH = "../assets/graphics/player/main_Idle.png"
    PLAYER_SPRITESHEET_PATH = "../assets/graphics/player/Char_008.png"
    MAP_PATH = "../assets/maps/map.txt"
    
    
    TILE_SIZE_32 = 32
    TILE_SIZE_48 = 48
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    SCALE_FACTOR = 1
    
    GRAVITY = 0.5

    # Add other global settings as needed
    FPS = 60
    BACKGROUND_COLOR = (0, 0, 0)  # Black
    
    PLAYER_SPEED = 2
    PLAYER_HEALTH = 100
    PLAYER_JUMP_STRENGTH = 8
    PLAYER_SIZE_48 = 48
    PLAYER_START_POSITION = [100, 100]

# Example usage:
# print(GameConfig.SPRITESHEET_PATH)
# print(GameConfig.TILE_SIZE)