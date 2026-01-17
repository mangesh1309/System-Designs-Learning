from abc import ABC, abstractmethod

# 1. Target Interface
class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# 2. Actual Interface (Adaptee)
class Razorpay:
    def make_payment(self, amount):
        print(f"Paid {amount} via Razorpay.")

# 3. Adapter
class RazorpayAdapter(PaymentGateway):
    def __init__(self, razorpay):
        self.razorpay = razorpay

    def pay(self, amount):
        self.razorpay.make_payment(amount)

# 4. Client Code
gateway = RazorpayAdapter(Razorpay())
gateway.pay(1500)