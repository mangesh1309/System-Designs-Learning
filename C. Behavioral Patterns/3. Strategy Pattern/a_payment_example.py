from abc import ABC, abstractmethod

# 1. Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self):
        pass

# 2. Concrete Strategies
class CardPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Paid ₹{amount} using Credit/Debit Card")

class UPIPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Paid ₹{amount} using UPI")

class WalletPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Paid ₹{amount} using Wallet")


# 3. Checkout Service
class PaymentService:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def make_payment(self, amount):
        self.strategy.pay(amount)


# 4. Client Code
if __name__ == "__main__":
    checkout = PaymentService(CardPayment())
    checkout.make_payment(1500)

    checkout.set_strategy(UPIPayment())
    checkout.make_payment(800)

    checkout.set_strategy(WalletPayment())
    checkout.make_payment(500)
