import pygame
from animation.animation import Animation
from physics.movement import Movement
from utils.game_config import GameConfig

class Player:
    def __init__(self, idle_sprite_sheet_path, move_sprite_sheet_path, jump_sprite_sheet_path, position, tile_size, map, player_size=GameConfig.PLAYER_SIZE_48, scale_factor=GameConfig.SCALE_FACTOR):
        self.idle_animation = Animation(idle_sprite_sheet_path, tile_size, scale_factor)
        self.move_animation = Animation(move_sprite_sheet_path, tile_size, scale_factor)
        self.jump_animation = Animation(jump_sprite_sheet_path, tile_size, scale_factor)
        self.movement = Movement(position, GameConfig.PLAYER_SPEED, GameConfig.PLAYER_JUMP_STRENGTH, player_size, scale_factor)  # Adjust jump strength as needed
        self.frame_index = 0
        self.animation_speed = 0.1  # Adjust animation speed as needed
        self.last_frame_update = pygame.time.get_ticks()
        self.map = map

    def update(self, keys, game_map):
        self.movement.update(keys, game_map)
        self.update_animation()

    def update_animation(self):
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.last_frame_update

        if elapsed_time > self.animation_speed * 1000:  # Convert animation speed to milliseconds
            if self.movement.is_jumping:
                self.frame_index = (self.frame_index + 1) % len(self.jump_animation.animations[self.movement.direction])
            elif self.movement.velocity.x != 0:
                self.frame_index = (self.frame_index + 1) % len(self.move_animation.animations[self.movement.direction])
            else:
                self.frame_index = (self.frame_index + 1) % len(self.idle_animation.animations[self.movement.direction])
            self.last_frame_update = current_time

    def draw(self, screen):
        if self.movement.is_jumping:
            current_frame = self.jump_animation.animations[self.movement.direction][self.frame_index]
        elif self.movement.velocity.x != 0:
            current_frame = self.move_animation.animations[self.movement.direction][self.frame_index]
        else:
            current_frame = self.idle_animation.animations[self.movement.direction][self.frame_index]
        screen.blit(current_frame, self.movement.position)
