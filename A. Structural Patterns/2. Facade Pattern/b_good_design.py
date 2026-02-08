
# 1. Reserve Seat
class SeatReservationService:
    def reserve_seat(self, movie_id, seat_number):
        print(f"Seat {seat_number} reserved for the movie {movie_id}")

# 2. Make Payment
class PaymentService:
    def make_payment(self, account_id, amount):
        print(f"Payment of ₹{amount} successful for account {account_id}")

# 3. Send Booking Notification
class NotificationService:
    def send_notification(self, user_email):
        print(f"Booking confirmation mail sent to {user_email}")

# 4. Add Loyal Points to User's Account
class LoyaltyPointsService:
    def add_points(self, account_id, points):
        print(f"{points} added to the account {account_id}")

# 5. Generate the ticket
class GenerateTicketService:
    def generate_ticket(self, movie_id, seat_number):
        print(f"Ticket generated for movie {movie_id}; {seat_number}")


# FACADE CLASS

class MovieTicketBookingFacade:
    def __init__(self):
        self.seat_reservation_service = SeatReservationService()
        self.payment_service = PaymentService()
        self.notification_service = NotificationService()
        self.loyalty_service = LoyaltyPointsService()
        self.ticket_service = GenerateTicketService()

    def book_ticket(self, movie_id, seat_number, account_id, user_email, amount):
        self.seat_reservation_service.reserve_seat(movie_id, seat_number)
        self.payment_service.make_payment(account_id, amount)
        self.notification_service.send_notification(user_email)
        self.loyalty_service.add_points(account_id, 10)
        self.ticket_service.generate_ticket(movie_id, seat_number)


# CLIENT CODE:

movie_id = "MOV123"
seat_number = "A10"
account_id = "ACC456"
user_email = "user@gmail.com"
ticket_price = 350

booking_facade = MovieTicketBookingFacade()

booking_facade.book_ticket(
    movie_id=movie_id,
    seat_number=seat_number,
    account_id=account_id,
    user_email=user_email,
    amount=ticket_price
)

# Clint does not have to worry abot instantiating each service and use
# Facade class does it for use