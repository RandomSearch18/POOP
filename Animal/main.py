class PetAnimal:
    name: str
    hunger: float
    boredness: float
    
    def __init__(self, name: str):
        self.name = name
        self.hunger = 0
        self.boredness = 0

    def eat(self):
        self.hunger = max(0, self.hunger - 0.5)
    
    def play(self):
        self.hunger = min(1, self.hunger + 0.1)
        self.boredness = max(1, self.boredness - 0.75)
    
