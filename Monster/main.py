class Monster:
    def __init__(self, poisonous: bool, strength: float, name: str):
        self._poisonous = poisonous
        self._strength = strength
        self._name = name
    
    def eat(self):
        print(f"{self._name} eats a hero. Yum!")
    
    def sleep(self):
        print("ZZzzzz ZZzzzzzzz")

    def greet(self):
        print(f"Hi, my name is {self._name}")

if __name__ == "__main__":
    monster_one = Monster(True, 5, "Oscar")
    monster_one = Monster(False, 5, "Charlie")
    print("Created two monsters")
