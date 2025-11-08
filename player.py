from base.base import Base
import pygame

class Player:
    def __init__(self, base_pos):
        self.gold = 100
        self.score = 0
        self.base = Base(base_pos)
        self.font = pygame.font.SysFont("Arial", 20)

    def earn_gold(self, amount):
        self.gold += amount

    def spend_gold(self, amount):
        if self.gold >= amount:
            self.gold -= amount
            return True
        return False

    def is_game_over(self):
        return self.base.is_destroyed()

    def draw_ui(self, screen):
        text = f"Gold: {self.gold}   HP: {self.base.hp}/{self.base.max_hp}   Score: {self.score}"
        img = self.font.render(text, True, (255, 255, 255))
        screen.blit(img, (20, 20))
