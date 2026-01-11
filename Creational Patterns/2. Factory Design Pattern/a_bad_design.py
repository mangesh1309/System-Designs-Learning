from abc import ABC, abstractmethod

class PaymentGateWayInterface(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass

class UPIPayment(PaymentGateWayInterface):
    def make_payment(self, amount):
        print(f"Paid {amount} successfully via UPI!")

class CashPayment(PaymentGateWayInterface):
    def make_payment(self, amount):
        print(f"Paid {amount} successfully via cash!")

class CardPayment(PaymentGateWayInterface):
    def make_payment(self, amount):
        print(f"Paid {amount} successfully via card!")


class PaymentFactory:
    def process_payment(self, amount, mode):
        # violates OCP
        if mode=="upi":
            # tigth coupling
            gateway = UPIPayment()
            gateway.make_payment(amount)
        elif mode=="cash":
            gateway = CashPayment()
            gateway.make_payment(amount)
        elif mode=="card":
            gateway = CardPayment()
            gateway.make_payment(amount)
        else:
            raise Exception("Invalid payment mode selected.")
    
try:
    payment_factory = PaymentFactory()
    payment_factory.process_payment(1500, "hand")
except Exception as e:
    print(e)