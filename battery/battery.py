from part import Part

class Battery(Part):
    def needs_service(self):
        # implement logic to determine if service is needed
        pass

class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.current_date = current_date

    def needs_service(self):
        return self.current_date - self.last_service_date > 2

class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.current_date = current_date

    def needs_service(self):
        return self.current_date - self.last_service_date > 4