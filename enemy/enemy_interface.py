import pygame
from abc import ABC, abstractmethod


class enemy_interface(ABC):

    @abstractmethod
    def update(self, base):
        pass

    @abstractmethod
    def draw(self, screen: pygame.Surface):
        pass

    @abstractmethod
    def take_damage(self, dmg: float) -> bool:
        pass

