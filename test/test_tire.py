import unittest
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire_conditions = [0,0,0,0.9]
        tire = CarriganTire(tire_conditions)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_conditions = [0,0,0,0.8]
        tire = CarriganTire(tire_conditions)
        self.assertFalse(tire.needs_service())

class TestOctoprime(unittest.TestCase):
    def test_needs_service_true(self):
        tire_conditions = [1,1,1,0]
        tire = OctoprimeTire(tire_conditions)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_conditions = [1,1,0,0]
        tire = OctoprimeTire(tire_conditions)
        self.assertFalse(tire.needs_service())
