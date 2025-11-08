import pygame
from towers.tower import Tower
import math

class TowerManager:
    def __init__(self, game_map):
        self.towers = []
        self.preview_pos = None
        self.map = game_map

        # 설치 거리 제한 (길 기준)
        self.min_distance_from_path = 40  # 너무 가까우면 X
        self.max_distance_from_path = 180  # 너무 멀면 X

    def can_place_tower(self, pos):
        # 기존 타워와 너무 가까운가?
        for t in self.towers:
            if math.dist(pos, t.pos) < 40:
                return False

        # 길에서의 거리 계산
        min_dist_to_path = float('inf')
        for p in self.map.path:
            dist = math.dist(pos, p)
            if dist < min_dist_to_path:
                min_dist_to_path = dist

        # 길에서 너무 가깝거나, 너무 멀면 설치 불가
        if min_dist_to_path < self.min_distance_from_path:
            return False
        if min_dist_to_path > self.max_distance_from_path:
            return False

        return True

    def handle_mouse(self, pos, player):
        # 설치 가능 여부 + 골드 확인
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
