import pygame
from map_interface import MapInterface

class ZigZagMap(MapInterface):
    def __init__(self):
        self.path = [
            (100, 100),
            (700, 100),
            (700, 250),
            (100, 250),
            (100, 400),
            (700, 400),
            (700, 550)
        ]

    def get_path(self):
        return self.path

    def get_base_position(self):
        return self.path[-1]

    def draw(self, screen):
        for i in range(len(self.path) - 1):
            pygame.draw.line(screen, (150, 150, 150), self.path[i], self.path[i+1], 40)
