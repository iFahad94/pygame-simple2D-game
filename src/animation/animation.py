import pygame

class Animation:
    def __init__(self, sprite_sheet_path, tile_size, scale_factor=1):
        self.sprite_sheet = pygame.image.load(sprite_sheet_path).convert_alpha()
        self.tile_size = tile_size
        self.scale_factor = scale_factor
        self.animations = self.load_animations()

    def load_animations(self):
        animations = {
            'down': [],
            'left': [],
            'right': [],
            'up': []
        }
        for direction, row in zip(animations.keys(), range(4)):
            for i in range(4):  # Assuming 4 frames per direction
                frame = self.get_image(i, row)
                animations[direction].append(frame)
        return animations

    def get_image(self, frame_index, row):
        rect = pygame.Rect(frame_index * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size)
        image = pygame.Surface((self.tile_size, self.tile_size), pygame.SRCALPHA)
        image.blit(self.sprite_sheet, (0, 0), rect)
        image = pygame.transform.scale(image, (self.tile_size * self.scale_factor, self.tile_size * self.scale_factor))
        return image
