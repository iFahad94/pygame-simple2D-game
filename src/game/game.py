import pygame
from chars.player import Player
from utils.game_config import GameConfig
from gui.main_menu import MainMenu
from gui.options_menu import OptionsMenu
from game.game_map import GameMap  # Adjust the import path

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = "start_menu"
        self.game_map = GameMap()  # Initialize the GameMap instance
        self.player = Player(GameConfig.PLAYER_SPRITESHEET_IDLE_PATH, GameConfig.PLAYER_SPRITESHEET_PATH,GameConfig.PLAYER_SPRITESHEET_PATH, GameConfig.PLAYER_START_POSITION, GameConfig.TILE_SIZE_32, self.game_map)
        self.main_menu = MainMenu(self.screen, self.start_game, self.show_options, self.quit_game)
        self.options_menu = OptionsMenu(self.screen, self.show_main_menu)

    def update(self):
        if self.state == "start_menu":
            self.main_menu.handle_events()
        elif self.state == "options_menu":
            self.options_menu.handle_events()
        elif self.state == "main_game":
            self.handle_game_events()

    def draw(self):
        if self.state == "start_menu":
            self.main_menu.display()
        elif self.state == "options_menu":
            self.options_menu.display()
        elif self.state == "main_game":
            self.display_game()

    def start_game(self):
        self.state = "main_game"

    def show_options(self):
        self.state = "options_menu"

    def show_main_menu(self):
        self.state = "start_menu"

    def quit_game(self):
        self.running = False

    def handle_game_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()
        self.player.update(keys, self.game_map)

    def display_game(self):
        self.screen.fill(GameConfig.BACKGROUND_COLOR)
        self.game_map.draw(self.screen)  # Draw the map
        self.player.draw(self.screen)
        pygame.display.flip()
