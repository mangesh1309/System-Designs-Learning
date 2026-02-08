from abc import ABC, abstractmethod

# 1: Target Interface (Expected by client)
class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# 2. Actaul Interface (Third party sdk)
class Razorpay:
    def make_payment(self, amount):
        print(f"Paid {amount} via Razorpay.")


# ❌ Issue
# Razorpay has make_payment
# Client expects pay
# Client breaks