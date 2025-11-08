import pygame
from map_interface import MapInterface

class StraightMap(MapInterface):
    def __init__(self):
        self.path = [(400, y) for y in range(50, 550, 50)]

    def get_path(self):
        return self.path

    def get_base_position(self):
        return self.path[-1] # 마지막 경로가 base

    def draw(self, screen):
        for i in range(len(self.path) - 1):
            pygame.draw.line(screen, (120, 120, 120), self.path[i], self.path[i+1], 40)
