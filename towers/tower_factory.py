from towers.basic_tower import BasicTower
from towers.slow_tower import SlowTower


class TowerFactory:
    tower_types = {
        "자연과학관": BasicTower,
        "어문학관": SlowTower
    }

    @staticmethod
    def create_tower(tower_type, pos):
        cls = TowerFactory.tower_types.get(tower_type)
        if cls is None:
            print("Unknown tower type:", tower_type)
            return None
        return cls(pos)
