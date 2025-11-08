import pygame

class Map:
    def __init__(self):
        self.path = [(100 + i * 5, 300) for i in range(120)]

    def draw(self, screen):
        for point in self.path:
            pygame.draw.circle(screen, (80, 80, 80), point, 3)
