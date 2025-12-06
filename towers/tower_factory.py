from towers.basic_tower import BasicTower
from towers.slow_tower import SlowTower


class TowerFactory:
    tower_types = {
        "basic": BasicTower,
        "slow": SlowTower
    }

    @staticmethod
    def create_tower(tower_type, pos):
        cls = TowerFactory.tower_types.get(tower_type)
        if cls is None:
            print("Unknown tower type:", tower_type)
            return None
        return cls(pos)
