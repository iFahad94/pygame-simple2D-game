import pygame

from utils.game_config import GameConfig
class Physics:
    def __init__(self, position, tile_size):
        self.position = pygame.Vector2(position)
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)
        self.on_ground = False
        self.tile_size = tile_size
        self.gravity = GameConfig.GRAVITY

    def apply_gravity(self):
        if not self.on_ground:
            self.acceleration.y += self.gravity

    def check_collision(self, map_data):
        # Implement collision detection logic here
        pass