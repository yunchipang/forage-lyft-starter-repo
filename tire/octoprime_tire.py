from .tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, tire_conditions):
        super().__init__()
        self.tire_conditions = tire_conditions

    def needs_service(self):
        total = 0
        for tire in self.tire_conditions:
            total += tire
        return total >= 3
