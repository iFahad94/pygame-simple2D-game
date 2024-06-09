# tileviewer.py
import pygame
from tile_manager import TileManager

class TileViewer:
    def __init__(self, tileset_path, tile_size):
        pygame.init()
        self.screen = pygame.display.set_mode((512, 512))
        self.clock = pygame.time.Clock()
        self.tile_manager = TileManager(tileset_path, tile_size)
        self.tiles = self.tile_manager.get_all_tiles()
        self.current_tile_index = 0
        self.font = pygame.font.SysFont(None, 24)  # Initialize a font for rendering text
        pygame.time.set_timer(pygame.USEREVENT, 1000)  # Set a custom event to trigger every second

    def render_text(self, text, position):
        text_surface = self.font.render(text, True, (255, 255, 255))  # Render text in white color
        self.screen.blit(text_surface, position)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.USEREVENT:  # Custom event to change the tile
                    self.current_tile_index = (self.current_tile_index + 1) % len(self.tiles)

            self.screen.fill((0, 0, 0))  # Fill screen with black

            # Display the current tile
            tile_image = self.tiles[self.current_tile_index]
            tile_rect = tile_image.get_rect(center=(256, 256))  # Center the tile in the window
            self.screen.blit(tile_image, tile_rect.topleft)

            # Display the tile index above the tile
            index_text = f"Tile Index: {self.current_tile_index}"
            text_position = (256 - tile_rect.width // 2, 256 - tile_rect.height // 2 - 20)  # Adjust position as needed
            self.render_text(index_text, text_position)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

# Example usage
if __name__ == "__main__":
    viewer = TileViewer('assets/graphics/Dungeon_Tileset.png', 32)  # Adjust the path and tile size as needed
    viewer.run()