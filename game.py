import pygame
import time
from towers.tower_manager import TowerManager
from player import Player
from levels.level_manager import LevelManager
from ui.tower_selection_ui import TowerSelectionUI

class Game:
    def __init__(self):
        pygame.init()
        info = pygame.display.Info()
        self.WIDTH = info.current_w
        self.HEIGHT = info.current_h
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.running = True
        self.level_manager = LevelManager(self.WIDTH, self.HEIGHT)
        self.load_level()
        self.tower_ui = TowerSelectionUI()
        self.selected_tower_type = None
        self.waiting_for_next_level = False
        self.next_level_time = 0
        self.level_clear_delay = 3

    def on_tower_selected(self, tower_name):
        self.selected_tower_type = tower_name

    def load_level(self):
        self.map, self.wave_manager = self.level_manager.load_map_and_wave()
        self.player = Player(self.map.get_base_position())
        self.tower_manager = TowerManager(self.map)
        self.projectiles = []

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    self.tower_ui.open(self.on_tower_selected)
                    return
            if event.type == pygame.MOUSEMOTION:
                self.tower_manager.preview_pos = event.pos

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.tower_ui.active:
                    self.tower_ui.handle_event(event)
                    return
                if self.selected_tower_type:
                    self.tower_manager.place_tower(
                        self.selected_tower_type, event.pos, self.player
                    )
                    return

    def update(self):
        if self.player.is_game_over():
            self.running = False
            return
        if self.waiting_for_next_level:
            if time.time() < self.next_level_time:
                return
            if self.level_manager.next_level():
                self.load_level()
            else:
                self.running = False
            self.waiting_for_next_level = False
            return

        self.wave_manager.update(self.player.base)
        new_proj = self.tower_manager.update(self.wave_manager.enemies, self.player)
        self.projectiles.extend(new_proj)
        for proj in self.projectiles[:]:
            proj.update()
            if not proj.alive:
                self.projectiles.remove(proj)

        if self.wave_manager.is_wave_cleared():
            self.waiting_for_next_level = True
            self.next_level_time = time.time() + self.level_clear_delay

    def draw(self):
        self.screen.fill((30, 30, 30))
        self.map.draw(self.screen)
        self.player.base.draw(self.screen)
        self.wave_manager.draw(self.screen)
        self.tower_manager.draw(self.screen)
        for proj in self.projectiles:
            proj.draw(self.screen)
        self.player.draw_ui(self.screen)
        self.tower_ui.draw(self.screen)
        if self.waiting_for_next_level:
            font = pygame.font.Font(None, 48)
            text = font.render("Level Cleared!", True, (255, 255, 0))
            self.screen.blit(text, (290, 260))

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
