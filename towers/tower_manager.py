import pygame
import math
from towers.tower_factory import TowerFactory

class TowerManager:
    def __init__(self, game_map):
        self.towers = []
        self.preview_pos = None
        self.map = game_map
        self.min_distance_from_path = 40
        self.max_distance_from_path = 180

    def point_to_segment_dist(self, px, py, x1, y1, x2, y2):
        A = pygame.math.Vector2(x1, y1)
        B = pygame.math.Vector2(x2, y2)
        P = pygame.math.Vector2(px, py)
        AB = B - A
        AP = P - A
        t = AB.dot(AP) / AB.length_squared()
        if t < 0.0:
            return AP.length()
        elif t > 1.0:
            return (P - B).length()
        else:
            projection = A + AB * t
            return (P - projection).length()

    def can_place_tower(self, pos):
        px, py = pos
        for t in self.towers:
            if math.dist(pos, t.pos) < 40:
                return False
        min_dist_to_path = float('inf')
        for i in range(len(self.map.path) - 1):
            x1, y1 = self.map.path[i]
            x2, y2 = self.map.path[i + 1]
            dist = self.point_to_segment_dist(px, py, x1, y1, x2, y2)
            min_dist_to_path = min(min_dist_to_path, dist)
        if min_dist_to_path < self.min_distance_from_path:
            return False
        if min_dist_to_path > self.max_distance_from_path:
            return False
        return True

    def place_tower(self, tower_type, pos, player):

        tower = TowerFactory.create_tower(tower_type, pos)
        if not tower or player.gold < tower.COST or not self.can_place_tower(pos):
            return False

        player.spend_gold(tower.COST)
        self.towers.append(tower)
        print(f"{tower_type} 타워 설치 완료!")
        return True

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

        if self.preview_pos:
            color = (0, 255, 0) if self.can_place_tower(self.preview_pos) else (255, 0, 0)
            pygame.draw.circle(screen, color, self.preview_pos, 20, 2)
