import pygame
from maps.map import Map
from tiles.tile_manager import TileManager
from utils.game_config import GameConfig

class GameMap:
    def __init__(self):
        self.tile_size = GameConfig.TILE_SIZE
        self.map = Map(GameConfig.MAP_PATH)
        self.tile_manager = TileManager(GameConfig.TILE_SET_PATH, self.tile_size)

    def draw(self, screen):
        for y, row in enumerate(self.map.tiles):
            for x, tile_id in enumerate(row):
                tile_image = self.tile_manager.get_tile_image(tile_id)
                screen.blit(tile_image, (x * self.tile_size, y * self.tile_size))

    def is_obstacle(self, x, y):
        if 0 <= y < len(self.map.tiles) and 0 <= x < len(self.map.tiles[y]):
            cell_value = self.map.tiles[y][x]
            return cell_value != 17
        return True  # Consider positions outside the map boundary as obstacles

    def is_walkable(self, x, y):
        return not self.is_obstacle(x, y)
