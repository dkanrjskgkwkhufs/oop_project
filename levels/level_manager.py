from enemys.enemy_exam import EnemyExam
from enemys.enemy_lateness import EnemyLateness
from enemys.enemy_snooze import EnemySnooze
from levels.level import Level
from maps.campus_map import CampusMap
from waves.wave_manager import WaveManager
from maps.straight_map import StraightMap
from maps.zigzag_map import ZigZagMap
from enemys.enemy_attendance import EnemyAttendance
from enemys.enemy_cplus import EnemyCplus

class LevelManager:
    def __init__(self, width, height):
        self.levels = [
            Level(1, "campus", waves=50, enemy_types=[(EnemyCplus, 50), (EnemyAttendance, 50)]),
            Level(2, "campus", waves=50, enemy_types=[(EnemyAttendance, 50), (EnemyLateness, 30), (EnemySnooze, 20)]),
            Level(3, "campus", waves=50, enemy_types=[(EnemyLateness, 70), (EnemyExam, 30)]),
        ]
        self.current_level_index = 0
        self.current_wave_manager = None
        self.width = width
        self.height = height

    def get_current_level(self):
        return self.levels[self.current_level_index]

    def next_level(self):
        if self.current_level_index + 1 < len(self.levels):
            self.current_level_index += 1
            return True
        return False  # 더 이상 레벨 없음

    def load_map_and_wave(self):
        level = self.get_current_level()
        if level.map_type == "straight":
            game_map = StraightMap()
        elif level.map_type == "zigzag":
            game_map = ZigZagMap()
        elif level.map_type == "campus":
            game_map = CampusMap(self.width, self.height)
        else:
            raise ValueError("Unknown map type")
        self.current_wave_manager = WaveManager(
            game_map.get_path(),
            total_enemies=level.waves,
            enemy_types=level.enemy_types
        )
        return game_map, self.current_wave_manager
