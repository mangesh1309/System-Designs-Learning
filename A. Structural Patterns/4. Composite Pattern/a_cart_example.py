# ItemInterface
# Product: implements ItemInterface
# ProductBundle: implements ItemInterface
# Cart
# Client Code


from abc import ABC, abstractmethod

class ItemInterface(ABC):
    @abstractmethod
    def get_name(self):
        pass
    
    @abstractmethod
    def get_price(self):
        pass

class Product(ItemInterface):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price

class ProductBundle(ItemInterface):
    def __init__(self, name):
        self.bundle_name = name
        self.items = []
    
    def get_name(self):
        return self.bundle_name

    def get_price(self):
        total = 0 # Composite pattern
        for item in self.items:
            total += item.get_price()

        return total

class Cart:
    def __init__(self):
        self.cart_items = []
    
    def add_item(self, item: ItemInterface):
        self.cart_items.append(item)

    def remove_item(self,item: ItemInterface):
        self.cart_items.remove(item)
    
    def get_total_price(self):
        total = 0 # Composite pattern
        for item in self.cart_items:
            total += item.get_price()
        return total

        #can write one liner as return sum(item.get_price() for item in self.cart_items)
    
    def show_items(self):
        for item in self.cart_items:
            print(f"{item.get_name()} - ${item.get_price()}")

# CLIENT CODE

cart = Cart()
cart.add_item(Product("Laptop", 1000))
cart.add_item(Product("Mouse", 100))
cart.add_item(ProductBundle("Bundle 1"))

cart.add_item(Product("Protein Bar", 100))

cart.show_items()
print(f"Total price: ${cart.get_total_price()}")
