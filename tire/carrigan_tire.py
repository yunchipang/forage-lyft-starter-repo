from .tire import Tire


class CarriganTire(Tire):
    def __init__(self, tire_conditions):
        super().__init__()
        self.tire_conditions = tire_conditions

    def needs_service(self):
        for tire in self.tire_conditions:
            if tire >= 0.9:
                return True
        return False