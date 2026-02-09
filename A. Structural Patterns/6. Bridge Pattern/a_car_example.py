# Problem:
# We have different types of cars (SUV, Hatchback, Sedan, etc.) and different types of engines (Petrol, Diesel, Electric, etc.). We want to create a flexible design where we can independently modify the car types and engine types without creating an explosion of classes. The Bridge pattern allows us to achieve this flexibility.

# **********************************************************************

# Components:
# Abstraction (Car): Represents the general concept of a car and holds a reference to an engine.
# Refined Abstraction (SUV, Hatchback, etc.): Concrete car types that extend the basic abstraction.
# Implementor (Engine): Represents the engine interface, defining methods like start() and stop().
# Concrete Implementor (Petrol, Diesel, Electric engines): Concrete implementations of the Engine interface, providing the specific logic for each engine type.



# 1. Implementor (Engine): Represents the engine interface, defining methods like start() and stop().
from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

# 2. Concrete Implementor (Petrol, Diesel, Electric engines): Concrete implementations of the Engine interface, providing the specific logic for each engine type.
class PetrolEngine(Engine):
    def start(self):
        print("Petrol Engine started.")
    
    def stop(self):
        print("Petrol Engine stopped.")

class DieselEngine(Engine):
    def start(self):
        print("Diesel Engine started.")
    
    def stop(self):
        print("Diesel Engine stopped.")

class ElectricEngine(Engine):
    def start(self):
        print("Electric Engine started.")
    
    def stop(self):
        print("Electric Engine stopped.")

# 3. Abstraction (Car): Represents the general concept of a car and holds a reference to an engine.
class Car(ABC):
    def __init__(self, engine: Engine):
        self.engine = engine  # The bridge between car type and engine
    
    @abstractmethod
    def display(self):
        pass
    
    def start(self):
        self.engine.start()
    
    def stop(self):
        self.engine.stop()

# 4. Refined Abstraction (SUV, Hatchback, etc.): Concrete car types that extend the basic abstraction.
class SUV(Car):
    def display(self):
        print("This is an SUV.")
        self.start()
        self.stop()

class Hatchback(Car):
    def display(self):
        print("This is a Hatchback.")
        self.start()
        self.stop()

class Sedan(Car):
    def display(self):
        print("This is a Sedan.")
        self.start()
        self.stop()
