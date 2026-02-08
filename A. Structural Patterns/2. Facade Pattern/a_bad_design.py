# Consider a step by step process of booking a movie ticket
# 1. Reserve Seat
# 2. Make Payment
# 3. Send Booking Notification
# 4. Add Loyal Points to User's Account
# 5. Generate the ticket

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


# CLIENT CODE (WITHOUT FACADE)

movie_id = "MOV123"
seat_number = "A10"
account_id = "ACC456"
user_email = "user@gmail.com"
ticket_price = 350

# Step 1: Reserve Seat
seat_reservation_service = SeatReservationService()
seat_reservation_service.reserve_seat(movie_id, seat_number)

# Step 2: Make Payment
payment_service = PaymentService()
payment_service.make_payment(account_id, ticket_price)

# Step 3: Send Booking Notification
notification_service = NotificationService()
notification_service.send_notification(user_email)

# Step 4: Add Loyalty Points
loyalty_service = LoyaltyPointsService()
loyalty_service.add_points(account_id, 10)

# Step 5: Generate Ticket
ticket_service = GenerateTicketService()
ticket_service.generate_ticket(movie_id, seat_number)


# ❌ Problems here

# 1. Client knows too many steps
# 2. Client controls execution order
# 3. Any change affects all clients
# 4. Logic duplicated across codebase