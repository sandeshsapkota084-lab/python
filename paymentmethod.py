from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentGateway):
    def pay(self, amount):
        print(f"Paying ${amount} via Credit Card.")

class PayPalPayment(PaymentGateway):
    def pay(self, amount):
        print(f"Paying ${amount} via PayPal.")

class CryptoPayment(PaymentGateway):
    def pay(self, amount):
        print(f"Paying ${amount} via Bitcoin.")

class GooglePayPayment(PaymentGateway):
    def pay(self, amount):
        print(f"Paying ${amount} via Google Pay.")

class ApplePayPayment(PaymentGateway):
    def pay(self, amount):
        print(f"Paying ${amount} via Apple Pay.")

class CheckoutService:
    def __init__(self):
        self.gateway = None

    def set_gateway(self, gateway):
        self.gateway = gateway

    def checkout(self, amount):
        print("Processing payment...")
        self.gateway.pay(amount)

service = CheckoutService()
service.set_gateway(CreditCardPayment())
service.checkout(120.00)
service.set_gateway(PayPalPayment())
service.checkout(75.50)
service.set_gateway(CryptoPayment())
service.checkout(200.00)