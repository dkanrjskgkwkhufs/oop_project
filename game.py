import pygame
from straight_map import StraightMap
from zigzag_map import ZigZagMap
from tower_manager import TowerManager
from wave_manager import WaveManager
from player import Player

class Game:
    def __init__(self, map_type="zigzag"):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Tower Defense - Multi Map")
        self.clock = pygame.time.Clock()
        self.running = True
        if map_type == "straight":
            self.map = StraightMap()
        elif map_type == "zigzag":
            self.map = ZigZagMap()
        else:
            raise ValueError("Unknown map type")

        self.player = Player(self.map.get_base_position())
        self.wave_manager = WaveManager(self.map.get_path())
        self.tower_manager = TowerManager(self.map)
        self.projectiles = []

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEMOTION:
                self.tower_manager.preview_pos = event.pos
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.tower_manager.handle_mouse(event.pos, self.player)

    def update(self):
        if self.player.is_game_over():
            print("Game Over!")
            self.running = False
            return

        self.wave_manager.update(self.player.base)
        new_proj = self.tower_manager.update(self.wave_manager.enemies, self.player)
        self.projectiles.extend(new_proj)
        for proj in self.projectiles[:]:
            proj.update()
            if not proj.alive:
                self.projectiles.remove(proj)

    def draw(self):
        self.screen.fill((30, 30, 30))
        self.map.draw(self.screen)
        self.player.base.draw(self.screen)
        self.wave_manager.draw(self.screen)
        self.tower_manager.draw(self.screen)
        for proj in self.projectiles:
            proj.draw(self.screen)
        self.player.draw_ui(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
