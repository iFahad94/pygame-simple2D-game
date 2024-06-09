import pygame
from game.game import Game
from utils.game_config import GameConfig

def main():
    pygame.init()
    screen = pygame.display.set_mode((GameConfig.SCREEN_WIDTH, GameConfig.SCREEN_HEIGHT))
    game = Game(screen)

    while game.running:
        game.update()
        game.draw()
        pygame.display.flip()
        game.clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
