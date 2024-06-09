import pygame
from utils.game_config import GameConfig

class MainMenu:
    def __init__(self, screen, start_callback, options_callback, quit_callback):
        self.screen = screen
        self.start_callback = start_callback
        self.options_callback = options_callback
        self.quit_callback = quit_callback
        self.start_button = None
        self.options_button = None
        self.quit_button = None

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_callback()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_button.collidepoint(event.pos):
                    self.start_callback()
                if self.options_button.collidepoint(event.pos):
                    self.options_callback()
                if self.quit_button.collidepoint(event.pos):
                    self.quit_callback()

    def display(self):
        self.screen.fill((0, 0, 0))
        title_font = pygame.font.Font(None, 74)  # or specify a font file path instead of None for a custom font
        title_text = title_font.render(GameConfig.GAME_NAME, True, (255, 255, 255))

        self.screen.blit(title_text, (self.screen.get_width() // 2 - title_text.get_width() // 2, 100))

        self.start_button = self.draw_button(GameConfig.GUI_START_BTN, (self.screen.get_width() // 2, 250))
        self.options_button = self.draw_button(GameConfig.GUI_OPTION_BTN, (self.screen.get_width() // 2, 350))
        self.quit_button = self.draw_button(GameConfig.GUI_QUIT_BTN, (self.screen.get_width() // 2, 450))

        pygame.display.flip()

    def draw_button(self, text, position):
        button_font = pygame.font.Font(None, 36)
        button_text = button_font.render(text, True, (255, 255, 255))
        button_rect = button_text.get_rect(center=position)
        pygame.draw.rect(self.screen, (100, 100, 100), button_rect.inflate(20, 20))
        self.screen.blit(button_text, button_rect)
        return button_rect
