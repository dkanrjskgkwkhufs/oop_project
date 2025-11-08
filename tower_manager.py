import pygame
from tower import Tower
import math

class TowerManager:
    def __init__(self):
        self.towers = []
        self.preview_pos = None

    def can_place_tower(self, pos):
        # 다른 타워와의 거리로 중복 설치 방지
        for t in self.towers:
            if math.dist(pos, t.pos) < 40:
                return False
        return True

    def handle_mouse(self, pos, player):
        # 설치 가능 여부와 골드 확인
        if player.gold >= Tower.COST and self.can_place_tower(pos):
            player.spend_gold(Tower.COST)
            self.towers.append(Tower(pos))
            return True
        return False

    def update(self, enemies, player):
        projectiles = []
        for tower in self.towers:
            proj = tower.update(enemies, player)
            if proj:
                projectiles.append(proj)
        return projectiles

    def draw(self, screen):
        for tower in self.towers:
            tower.draw(screen)

        # 설치 미리보기 (마우스 위치)
        if self.preview_pos:
            color = (0, 255, 0) if self.can_place_tower(self.preview_pos) else (255, 0, 0)
            pygame.draw.circle(screen, color, self.preview_pos, 20, 2)
