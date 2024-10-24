from building import *
from utils.exceptions import NotEnoughResourcesError

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
    
    def can_afford(self, cost: dict):
        return all(self.resources[res] >= cost.get(res, 0) for res in cost)