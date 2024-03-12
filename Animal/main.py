class PetAnimal:
    name: str
    species: str
    hunger: float
    boredness: float
    color: list[str]

    def __init__(self, name: str, species: str, color: list[str]):
        self.name = name
        self.species = species
        self.color = color
        self.hunger = 0
        self.boredness = 0

    def eat(self):
        self.hunger = max(0, self.hunger - 0.5)

    def play(self):
        self.hunger = min(1, self.hunger + 0.1)
        self.boredness = max(1, self.boredness - 0.75)

    def tick(self):
        self.hunger += 0.1
        self.boredness += 0.1

    def __str__(self):
        return f"{self.species}('{self.name.capitalize()}')"


class Cat(PetAnimal):
    def __init__(self, name: str, fur_color: str):
        super().__init__(name, "cat", [fur_color])


class Lizard(PetAnimal):
    def __init__(self, name: str, colors: list[str]):
        super().__init__(name, "lizard", colors)


def main():
    daisy = Cat("daisy", "black")
    midnight = Cat("midnight", "black")
    bodhi = Cat("bodhi", "brown")
    the_other_one = Cat("gato numero 4", "white")

    print(daisy, midnight, bodhi, the_other_one)


if __name__ == "__main__":
    main()
