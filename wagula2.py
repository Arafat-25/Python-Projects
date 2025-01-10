import random

# Define a dictionary to store user information
users = {
    "0777123456": {"name": "John Doe", "balance": 1000},
    "0756789012": {"name": "Jane Doe", "balance": 500},
    "0789012345": {"name": "Bob Smith", "balance": 2000},
    # Add more users here
}

# Define a list to store mobile numbers
mobile_numbers = list(users.keys())

# Use a while loop to randomly select a winner
while True:
    winner_number = random.choice(mobile_numbers)
    print("Winner's Details:")
    print("Mobile Number:", winner_number)
    print("Name:", users[winner_number]["name"])
    print("Balance:", users[winner_number]["balance"])
    break

# Use a for loop to print all users' details
print("\nAll Users' Details:")
for number, user in users.items():
    print("Mobile Number:", number)
    print("Name:", user["name"])
    print("Balance:", user["balance"])
    print()