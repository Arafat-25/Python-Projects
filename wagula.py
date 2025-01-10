import random

# Pool of mobile numbers
mobile_numbers = ["0770000000", "0770000001", "0770000002", "0770000003", "0770000004"]

# Dictionary to store user details
users = {
    "1": {"name": "John Doe", "email": "johndoe@example.com", "mobile_number": "0770000000"},
    "2": {"name": "Jane Doe", "email": "janedoe@example.com", "mobile_number": "0770000001"},
    "3": {"name": "Bob Smith", "email": "bobsmith@example.com", "mobile_number": "0770000002"},
    "4": {"name": "Alice Johnson", "email": "alicejohnson@example.com", "mobile_number": "0770000003"},
    "5": {"name": "Mike Brown", "email": "mikebrown@example.com", "mobile_number": "0770000004"},
}

def pick_winner():
    # Randomly select a mobile number from the pool
    winner_number = random.choice(mobile_numbers)
    # Get the user details from the dictionary
    for key, value in users.items():
        if value['mobile_number'] == winner_number:
            winner_details = value
            break
    # Print the winner's details
    print(f"Winner: {winner_details['name']}")
    print(f"Mobile Number: {winner_number}")
    print(f"Email: {winner_details['email']}")

pick_winner()