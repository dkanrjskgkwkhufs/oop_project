import pygame
from maps.map_interface import MapInterface

class CampusMap(MapInterface):
    def __init__(self, width, height):
        bg = pygame.image.load("assets/map.png").convert()
        self.background = pygame.transform.scale(bg, (width, height))
        self.path = [
            (400, 650),
            (200, 650),
            (200, 510),
            (1000, 510),
            (1000, 370),
            (200, 370),
            (200, 280),
            (1000, 280),
            (1000, 180)
        ]



    def get_path(self):
        return self.path

    def get_base_position(self):
        return self.path[-1]

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
