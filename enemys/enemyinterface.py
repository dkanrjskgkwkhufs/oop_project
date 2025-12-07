import pygame
from abc import ABC, abstractmethod


class EnemyInterface(ABC):

    @abstractmethod
    def update(self, base):
        pass

    @abstractmethod
    def draw(self, screen: pygame.Surface):
        pass

    @abstractmethod
    def take_damage(self, dmg: float) -> bool:
        pass

    @abstractmethod
    def apply_slow(self, rate: float):
        pass