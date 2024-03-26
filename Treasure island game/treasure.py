class Treasure:
    value: int
    level: str

    def __init__(self, value: int, level: str):
        self._value = value
        self._level = level

    def get_value(self):
        return self._value

    def set_value(self, value: int):
        self._value = value

    def get_level(self):
        return self._level

    def set_level(self, level: str):
        self._level = level

    def __str__(self):
        level_part = self.get_level().capitalize()
        value_part = self.get_value()
        return f"{level_part} treasure (value {value_part})"


if __name__ == "__main__":
    bronze_treasure = Treasure(100, "bronze")
    bronze_treasure.set_value(150)
    bronze_treasure.set_level("ultra bronze")

    print(bronze_treasure)
