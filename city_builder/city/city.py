from building import *

class City:
    def __init__(self) -> None:
        self.buildings: list = []
        self.resources: dict = {
            'wood': 12,
            'stone': 0,
            'food': 6,
            'gold': 0,
            'resident': 3
        }
    
    def add_building(self, building) -> None:
        self.add_building(building)