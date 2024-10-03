class Building:
    def __init__(self, name: str, cost: dict, production: dict) -> None:
        self.name: str = name
        self.cost: dict = cost
        self.production: dict = production
        

class House(Building):
    def __init__(self):
        super().__init__(name="Ház", cost={'wood': 3, 'stone': 0, 'resident': 0}, production={'resident': 1})
        
class Farm(Building):
    def __init__(self):
        super().__init__(name="Farm", cost={'wood': 4, 'stone': 1, 'resident': 3}, production={"wheat": 8})
        
class Forest(Building):
    def __init__(self):
        super().__init__(name="Forest", cost={'wood': 2, 'stone': 0, 'resident': 1}, production={"wood": 3})
        
class Mill(Building):
    def __init__(self):
        super().__init__(name="Mill", cost={'wood': 5, 'stone': 3, 'resident': 2}, production={"flour": 5})
        
        
class Bakery(Building):
    def __init__(self):
        super().__init__(name="Bakery", cost={'wood': 4, 'stone': 1, 'resident': 2}, production={"food": 2})
        
class Mine(Building):
    def __init__(self):
        super().__init__(name="Mine", cost={'wood': 4, 'stone': 0, 'resident': 3}, production={"stone": 2})
        
class Hut(Building):
    def __init__(self):
        super().__init__(name="Hut", cost={'wood': 2, 'stone': 0, 'resident': 1}, production={"food": 1})
        
