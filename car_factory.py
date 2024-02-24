from car import Car
from parts import CapuletEngine, WilloughbyEngine, SternmanEngine, SpindlerBattery, NubbinBattery

class CarFactory:

    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine()
        battery = SpindlerBattery()
        return Car(engine, battery)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine()
        battery = SpindlerBattery()
        return Car(engine, battery)

    @staticmethod
    def create_palindrome(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = SternmanEngine()
        battery = SpindlerBattery()
        return Car(engine, battery)
    
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine()
        battery = NubbinBattery()
        return Car(engine, battery)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine()
        battery = NubbinBattery()
        return Car(engine, battery)


        