# tilemanage.py
import pygame

class TileManager:
    def __init__(self, tileset_path, tile_size):
        self.tileset = pygame.image.load(tileset_path).convert_alpha()
        self.tile_size = tile_size

    def get_tile_image(self, tile_id):
        tiles_per_row = self.tileset.get_width() // self.tile_size
        row = tile_id // tiles_per_row
        col = tile_id % tiles_per_row
        tile_rect = pygame.Rect(col * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size)
        tile_image = pygame.Surface(tile_rect.size, pygame.SRCALPHA)
        tile_image.blit(self.tileset, (0, 0), tile_rect)
        return tile_image

    def get_all_tiles(self):
        tiles = []
        tileset_width, tileset_height = self.tileset.get_size()
        tiles_per_row = tileset_width // self.tile_size
        tiles_per_col = tileset_height // self.tile_size

        for row in range(tiles_per_col):
            for col in range(tiles_per_row):
                tile_rect = pygame.Rect(col * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size)
                tile_image = pygame.Surface(tile_rect.size, pygame.SRCALPHA)
                tile_image.blit(self.tileset, (0, 0), tile_rect)
                tiles.append(tile_image)
        return tiles