import pygame
from abc import ABC, abstractmethod

class TowerInterface(ABC):
    @abstractmethod
    def update(self, enemies, player):
        pass

    @abstractmethod
    def draw(self, screen: pygame.Surface):
        pass

    @property
    @abstractmethod
    def cost(self):
        pass

    @property
    @abstractmethod
    def pos(self):
        pass
