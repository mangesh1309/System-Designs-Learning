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
    @staticmethod
    def get_payment_gateway(mode) -> PaymentGateWayInterface:
        if mode=="upi":
            return UPIPayment()
        elif mode=="cash":
            return CashPayment()
        elif mode=="card":
            return CardPayment()
        else:
            raise Exception("Error while making payment: Invalid payment mode selected.")

class PaymentService:
    def process_payment(self, mode, amount):
        try:
            gateway = PaymentFactory.get_payment_gateway(mode)
            gateway.make_payment(amount)
        except Exception as e:
            print(e)

payment_service = PaymentService()
payment_service.process_payment("cash", 2500)

# in GoF factory method, we can define creators: abstract creator having two methods, create_gateway(abs) and process payment(common method-concrete)
# each payment mode implements this abs creator and defines create_gateway method.