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
        return self.level

    def set_level(self, level: str):
        self._level = level
