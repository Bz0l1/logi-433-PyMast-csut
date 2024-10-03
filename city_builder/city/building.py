class Building:
    def __init__(self, name: str, cost: float, production: dict) -> None:
        self.name: str = name
        self.cost: float = cost
        self.production: dict = production
        

class House(Building):
    def __init__(self):
        super().__init__(name="Ház", cost=110, production={'resident': 3})
        
class Farm(Building):
    def __init__(self):
        super().__init__(name="Farm", cost=230, production={"wheat": 12})
        
class Forest(Building):
    def __init__(self):
        super().__init__(name="Forest", cost=150, production={"wood": 8})
        
class Mill(Build):
    def __init__(self):
        super().__init__(name="Mill", cost=260, production={"flour": 20})
        
        
class Bakery(Building):
    def __init__(self):
        super().__init__(name="Bakery", cost=230, production={"food": 5})
        
class Mine(Building):
    def __init__(self):
        super().__init__(name="Mine", cost=200, production={"stone": 20})
        
class Hut(Building):
    def __init__(self):
        super().__init__(name="Hut", cost=100, production={"food": 3})
        
