from abc import ABC, abstractmethod
import time

# SUBJECT INTERFACE
class DataService(ABC):
    @abstractmethod
    def fetch_data(self):
        pass

# REAL SUBJECT
class RealDataService(DataService):
    def fetch_data(self):
        print("Fetching data from the database...")
        time.sleep(2)
        print("Sensitive Data fetched successfully!")

# PROXY
class ProxyDataService(DataService):
    def __init__(self):
        self.__real_service = RealDataService()
    
    def fetch_data(self):
        if self.__real_service is None:
            self.__real_service = RealDataService()
        
        self.__real_service.fetch_data()

# CLIENT CODE
service = ProxyDataService()
service.fetch_data()


# Types of Proxy Patterns:
# 1. Virtual Proxy: Lazy initialization of expensive objects
# 2. Protection Proxy: Access control
# 3. Cache Proxy: Caching results
# 4. Logging Proxy: Logging requests
# 5. Transaction Proxy: Transaction management
# 6. Load Balancing Proxy: Load balancing