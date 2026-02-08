# You don’t want classes like:

# MilkCoffee
# MilkSugarCoffee
# MilkSugarCaramelCoffee
# MilkSugarCaramelWhippedCoffee

# BASE INTERFACE
from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass

# CONCRETE COMPONENT (BASE COFFEE)
class SimpleCoffee(Coffee):
    def cost(self):
        return 50
    
    def description(self):
        return "Simple Coffee"

# ABSTRACT DECORATOR
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee

# CONCRETE DECORATOR

# Milk Decorator
class Milk(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 20
    
    def description(self):
        return self.coffee.description() + ", Milk"

# Sugar Decorator
class Sugar(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 10

    def description(self):
        return self.coffee.description() + ", Sugar"

# Caramel Decorator
class Caramel(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 30
    
    def description(self):
        return self.coffee.description() + ", Caramel"
    

# CLIENT CODE
coffee = SimpleCoffee()
print(coffee.cost(), coffee.description())

coffee = Milk(coffee)
coffee = Sugar(coffee)
coffee = Caramel(coffee)

print(coffee.cost())
print(coffee.description())
