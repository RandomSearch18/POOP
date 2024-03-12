class Vector:
    def __init__(x: float, y: float) -> None:
        self.x = x
        self.y = y


class SpaceInvaderShip:
    def __init__(self) -> None:
        self.position = Vector(0, 0)
        self.velocity = Vector(0, 0)
