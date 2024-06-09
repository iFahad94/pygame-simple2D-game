import pygame

class TextureScaler:
    @staticmethod
    def enlarge(texture_surface):
        width, height = texture_surface.get_size()
        enlarged_surface = pygame.transform.scale(texture_surface, (width * 2, height * 2))
        return enlarged_surface
