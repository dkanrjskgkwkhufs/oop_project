import pygame

class Base:
    def __init__(self, position, hp=100):
        self.position = position
        self.max_hp = hp
        self.hp = hp
        self.radius = 30

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def is_destroyed(self):
        return self.hp <= 0

    def draw(self, screen):
        # 본체
        pygame.draw.circle(screen, (100, 150, 255), self.position, self.radius)

        # HP 바
        bar_w = 60
        bar_h = 8
        ratio = self.hp / self.max_hp
        pygame.draw.rect(screen, (50, 50, 50), (self.position[0] - bar_w//2, self.position[1] - 50, bar_w, bar_h))
        pygame.draw.rect(screen, (0, 200, 0), (self.position[0] - bar_w//2, self.position[1] - 50, int(bar_w * ratio), bar_h))
