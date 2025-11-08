from abc import ABC, abstractmethod
import pygame

class MapInterface(ABC):
    @abstractmethod
    def get_path(self):
        """적이 이동할 경로를 반환"""
        pass

    @abstractmethod
    def get_base_position(self):
        """기지(Base)의 위치 반환"""
        pass

    @abstractmethod
    def draw(self, screen):
        """맵을 그린다."""
        pass
