import pygame

from physics.physics import Physics
from utils.game_config import GameConfig

class Movement:
    def __init__(self, position, speed, jump_strength, player_size, scale_factor):
        self.position = position
        self.speed = speed
        self.jump_strength = jump_strength
        self.player_size = player_size
        self.scale_factor = scale_factor
        self.direction = 'right'
        self.moving_left = False
        self.moving_right = False
        self.is_jumping = False
        self.velocity = pygame.Vector2(0, 0)
        self.gravity = pygame.Vector2(0, 0.2)
        # self.physics = Physics(self, position, GameConfig.TILE_SIZE_32)

    def update(self, keys, game_map):
        self.handle_input(keys)
        self.move(game_map)

    def handle_input(self, keys):
        self.velocity.x = 0
        if keys[pygame.K_LEFT]:
            self.velocity.x = -self.speed
            self.direction = 'left'
            self.moving_left = True
        elif keys[pygame.K_RIGHT]:
            self.velocity.x = self.speed
            self.direction = 'right'
            self.moving_right = True
        else:
            self.moving_left = False
            self.moving_right = False

        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.velocity.y = -self.jump_strength
            self.is_jumping = True

    def move(self, game_map):
        self.position += self.velocity
        # self.physics.check_collision()
