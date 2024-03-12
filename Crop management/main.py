from math import inf
from random import randint
from typing import Callable
from enum import Enum
from inputs import integer, integer_range
from menu import Menu, MenuItem, wait_for_enter_key

class SimpleMenuItem(MenuItem):

    def __init__(self, label: str, callback: Callable, should_show: Callable[[], bool] | None = None, description: str | None = None):
        super().__init__(label, should_show, description)
        self.callback = callback
    
    def execute(self, error_handling):
        self.callback()

class CropStatus(Enum):
    SEED = "Seed"
    SEEDLING = "Seedling"
    YOUNG = "Young"
    MATURE = "Mature"
    OLD = "Old"

class CropType(Enum):
    GENERIC = "Generic"

class Crop:
    """A generic food crop"""
    def __init__(self, growth_rate: float, light_need: float, water_need: float) -> None:
        self._growth = 0
        self._days_growing = 0

        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = CropStatus.SEED
        self._type = CropType.GENERIC

    def grow(self, light: float, water: float):
        if light >= self._light_need and water >= self._water_need:
            # Provided amounts of light and water are adequate
            self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()

    def generate_report(self):
        """Returns a dictionary of information about the crop's current state"""
        return {
            "type": self._type.value,
            "status": self._status.value,
            "growth": f"{self._growth} day(s) growing"
        }
    
    def auto_grow(self, days: int):
        for _ in range(days):
            light = randint(1, 10)
            water = randint(1, 10)
            self.grow(light, water)

    def _update_status(self):
        """Changes the status of the crop based on its growth value"""
        if self._growth > 15:
            self._status = CropStatus.OLD
        elif self._growth > 10:
            self._status = CropStatus.MATURE
        elif self._growth > 5:
            self._status = CropStatus.YOUNG
        elif self._growth > 0:
            self._status = CropStatus.SEEDLING
        elif self._growth == 0:
            self._status = CropStatus.SEED
        else:
            raise ValueError(f"Crop growth value is invalid")

def manually_grow():
    global new_crop
    light_level = integer_range("Enter today's light level (1-10) ", 1, 10)
    water_level = integer_range("Enter today's water level (1-10) ", 1, 10)
    new_crop.grow(light_level, water_level)

def automatically_grow():
    global new_crop
    days = integer_range("How many days do you want to grow the crop for? ", 0, inf)
    new_crop.auto_grow(days)

def show_status_report():
    global new_crop
    print(new_crop.generate_report())
    print()
    wait_for_enter_key()

def show_main_menu():
    main_menu = Menu([
        SimpleMenuItem("Grow manually over 1 day", manually_grow),
        SimpleMenuItem("Grow automatically over multiple days", automatically_grow),
        SimpleMenuItem("Report status", show_status_report),
    ], title="Crop management program: Main menu")

    main_menu.show(loop=True)

def main():
    global new_crop
    new_crop = Crop(growth_rate=2, light_need=4, water_need=3)
    barley = Crop(growth_rate=3, light_need=6, water_need=4)

    new_crop.grow(light=6, water=6)
    print(new_crop.generate_report())

    show_main_menu()

if __name__ == "__main__":
    main()