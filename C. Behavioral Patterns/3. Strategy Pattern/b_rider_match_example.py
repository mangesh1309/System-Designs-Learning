from abc import ABC, abstractmethod

# ==============================
# Strategy Interface
# ==============================
class MatchingStrategy(ABC):
    @abstractmethod
    def match(self, rider_location):
        pass

# ==============================
# Concrete Strategy: Nearest Driver
# ==============================
class NearestDriverStrategy(MatchingStrategy):
    def match(self, rider_location):
        print(f"Matching with the nearest available driver to {rider_location}")
        # Distance-based matching logic

# ==============================
# Concrete Strategy: Airport Queue
# ==============================
class AirportQueueStrategy(MatchingStrategy):
    def match(self, rider_location):
        print(f"Matching using FIFO airport queue for {rider_location}")
        # Match first-in-line driver for airport pickup

# ==============================
# Concrete Strategy: Surge Priority
# ==============================
class SurgePriorityStrategy(MatchingStrategy):
    def match(self, rider_location):
        print(f"Matching rider using surge pricing priority near {rider_location}")
        # Prioritize high-surge zones or premium drivers

# ==============================
# Context Class: RideMatchingService
# ==============================
class RideMatchingService:
    def __init__(self, strategy):
        self.strategy = strategy  # Constructor injection of strategy

    def set_strategy(self, strategy):
        self.strategy = strategy  # Setter injection to change strategy dynamically

    def match_rider(self, location):
        self.strategy.match(location)  # Delegates the matching logic to the strategy

# ==============================
# Client Code
# ==============================
def main():
    # Using airport queue strategy
    ride_matching_service = RideMatchingService(AirportQueueStrategy())
    ride_matching_service.match_rider("Terminal 1")

    # Using nearest driver strategy and later switching to surge priority
    ride_matching_service2 = RideMatchingService(NearestDriverStrategy())
    ride_matching_service2.match_rider("Downtown")
    ride_matching_service2.set_strategy(SurgePriorityStrategy())
    ride_matching_service2.match_rider("Downtown")

if __name__ == "__main__":
    main()
