from abc import ABC, abstractmethod
import time

class PaymentService(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class RealPaymentService(PaymentService):
    def pay(self, amount):
        print(f"Processing Payment of ${amount}...")
        return "SUCCESS"

class LoggingPaymentProxy(PaymentService):
    def __init__(self, real_service: PaymentService):
        self.__real_service = real_service
    
    def pay(self, amount):
        start_time = time.time()
        print(f"[LOG] Payment of ${amount} started at {start_time}")

        result = self.__real_service.pay(amount)
        time.sleep(3)

        end_time = time.time()
        print(f"[LOG] Payment of ${amount} completed in {end_time - start_time} seconds")
        print(f"[LOG] Payment result: {result}")

        return result

# CLIENT CODE
real_service = RealPaymentService()
proxy_service = LoggingPaymentProxy(real_service)
proxy_service.pay(1200)