import pygame
from maps.map_interface import MapInterface

class CampusMap(MapInterface):
    def __init__(self):
        self.background = pygame.image.load("assets/map.png")
        self.background = pygame.transform.scale(self.background, (800, 600))
        self.path = [
            (200, 525),
            (150, 525),
            (150, 425),
            (600, 425),
            (600, 325),
            (100, 325),
            (100, 225),
            (600, 225),
            (600, 125)
        ]



    def get_path(self):
        return self.path

    def get_base_position(self):
        return self.path[-1]

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
