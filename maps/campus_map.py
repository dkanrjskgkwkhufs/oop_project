import pygame
from maps.map_interface import MapInterface

class CampusMap(MapInterface):
    def __init__(self, width, height):
        bg = pygame.image.load("assets/map.png").convert()
        self.background = pygame.transform.scale(bg, (width, height))
        self.path = [
            (324, 740),
            (202, 739),
            (208, 565),
            (980, 560),
            (977, 420),
            (204, 419),
            (209, 314),
            (980, 299),
            (971, 211)
        ]



    def get_path(self):
        return self.path

    def get_base_position(self):
        return self.path[-1]

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
