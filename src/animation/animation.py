import pygame

from utils.game_config import GameConfig

class Animation:
    def __init__(self, sprite_sheet_path, player_width, player_height, scale_factor=GameConfig.SCALE_FACTOR):
        self.sprite_sheet = pygame.image.load(sprite_sheet_path).convert_alpha()
        self.player_width = player_width
        self.player_height = player_height
        self.scale_factor = scale_factor
        self.animations = self.load_animations()

    def load_animations(self):
        animations = {
            'left': [],
            'right': [],
            'jump' : []
        }
        for direction, row in zip(animations.keys(), range(10)):
            for i in range(10):
                frame = self.get_image(i, row)
                animations[direction].append(frame)
        return animations

    def get_image(self, frame_index, row):
        rect = pygame.Rect(frame_index * self.player_width, row * self.player_height, self.player_width, self.player_height)
        image = pygame.Surface((self.player_width, self.player_height), pygame.SRCALPHA)
        image.blit(self.sprite_sheet, (0, 0), rect)
        return image
    
    def update_animation(self, is_jumping, is_moving):
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.last_frame_update

        if elapsed_time > self.animation_speed * 1000:  # Convert animation speed to milliseconds
            if is_jumping:
                self.frame_index = (self.frame_index + 1) % len(self.jump_animation.animations[self.movement.direction])
            elif self.is_moving:
                self.frame_index = (self.frame_index + 1) % len(self.move_animation.animations[self.movement.direction])
            else:
                self.frame_index = (self.frame_index + 1) % len(self.idle_animation.animations[self.movement.direction])
            self.last_frame_update = current_time
