total_seats = 50
available_seats = total_seats
price_per_ticket = 10

print("Welcome to Movie Theater Ticket Booking")
num_tickets = int(input("Enter the number of tickets you want to book: "))

if num_tickets > 0:
    if num_tickets <= available_seats:
        total_cost = num_tickets * price_per_ticket
        print(f"Total cost for {num_tickets} tickets: ${total_cost}")
        available_seats -= num_tickets
        print(f"{num_tickets} tickets booked. Available seats now: {available_seats}")
    else:
        print(f"Sorry, only {available_seats} tickets available.")
else:
    print("Invalid number of tickets. Please enter a valid number.")