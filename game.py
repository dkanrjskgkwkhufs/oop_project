import pygame
from map import Map
from wave_manager import WaveManager
from player import Player
from tower_manager import TowerManager

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Tower Defense - Build System")
        self.clock = pygame.time.Clock()
        self.running = True

        self.map = Map()
        self.player = Player(self.map.path[-1])
        self.wave_manager = WaveManager(self.map.path)
        self.tower_manager = TowerManager()
        self.projectiles = []

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.MOUSEMOTION:
                self.tower_manager.preview_pos = event.pos

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # 왼쪽 클릭 시 타워 설치 시도
                success = self.tower_manager.handle_mouse(event.pos, self.player)
                if not success:
                    print("💸 설치 실패 (골드 부족 or 위치 불가)")

    def update(self):
        if self.player.is_game_over():
            print("Game Over!")
            self.running = False
            return

        # 적 업데이트
        self.wave_manager.update(self.player.base)

        # 타워 업데이트
        new_proj = self.tower_manager.update(self.wave_manager.enemies, self.player)
        self.projectiles.extend(new_proj)

        # 투사체 업데이트
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
