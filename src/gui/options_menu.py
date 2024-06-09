import pygame
from utils.game_config import GameConfig

class OptionsMenu:
    def __init__(self, screen, back_callback):
        self.screen = screen
        self.back_callback = back_callback
        self.back_button = None

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.back_callback()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_button.collidepoint(event.pos):
                    self.back_callback()

    def display(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 74)
        text = font.render("Options", True, (255, 255, 255))
        self.screen.blit(text, (self.screen.get_width() // 2 - text.get_width() // 2, 100))

        self.back_button = self.draw_button("Back", (self.screen.get_width() // 2, 450))
        pygame.display.flip()

    def draw_button(self, text, position):
        button_font = pygame.font.Font(None, 36)
        button_text = button_font.render(text, True, (255, 255, 255))
        button_rect = button_text.get_rect(center=position)
        pygame.draw.rect(self.screen, (100, 100, 100), button_rect.inflate(20, 20))
        self.screen.blit(button_text, button_rect)
        return button_rect
