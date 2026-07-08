from abc import ABC, abstractmethod

class ShippingMethod(ABC):
    @abstractmethod
    def calculate(self, weight_kg):
        pass

class StandardShipping(ShippingMethod):
    def calculate(self, weight_kg):
        cost = 5.00 + (weight_kg * 1.50)
        print(f"Standard Shipping: ${cost:.2f} (Weight: {weight_kg}kg)")

class ExpressShipping(ShippingMethod):
    def calculate(self, weight_kg):
        cost = 15.00 + (weight_kg * 3.00)
        print(f"Express Shipping: ${cost:.2f} (Weight: {weight_kg}kg)")

class DroneDelivery(ShippingMethod):
    def calculate(self, weight_kg):
        cost = 20.00 + (weight_kg * 4.50)
        print(f"Drone Delivery: ${cost:.2f} (Weight: {weight_kg}kg)")

class InternationalPriorityShipping(ShippingMethod):
    def calculate(self, weight_kg):
        cost = 50.00 + (weight_kg * 10.00)
        print(f"International Priority Shipping: ${cost:.2f} (Weight: {weight_kg}kg)")

class SameDayDelivery(ShippingMethod):
    def calculate(self, weight_kg):
        cost = 25.00 + (weight_kg * 5.00)
        print(f"Same-Day Delivery: ${cost:.2f} (Weight: {weight_kg}kg)")

class ShippingCalculator:
    def __init__(self):
        self.method = None

    def set_method(self, method):
        self.method = method

    def calculate_cost(self, weight_kg):
        print("Calculating shipping cost...")
        self.method.calculate(weight_kg)

calculator = ShippingCalculator()
calculator.set_method(StandardShipping())
calculator.calculate_cost(2.5)
calculator.set_method(ExpressShipping())
calculator.calculate_cost(2.5)
calculator.set_method(DroneDelivery())
calculator.calculate_cost(2.5)
calculator.set_method(InternationalPriorityShipping())
calculator.calculate_cost(2.5)
calculator.set_method(SameDayDelivery())
calculator.calculate_cost(2.5)