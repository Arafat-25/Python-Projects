#importing date and time module to display the current date
import datetime

#Defualt starting amount
mtn_balance=500000
airtel_balance=100000


send_charge_mtn=0.05
send_charge_airtel=0.03
withdraw_charge_mtn=0.03
withdraw_charge_airtel=0.02
tax_rate=0.06

def send_charges(amount,charge):
    return amount*charge

def withdraw_charge(amount,charge):
    return amount*charge

def Tax_rate(amount):
    return amount*tax_rate

def main():
    current_date=datetime.datetime.today
    print(current_date)



    print(f"Welcome to Mobile money transactions.",{current_date})
    print("Choose your operator.")
    print("1. MTN")
    print("2. Airtel")

operator=input("Enter your choice (MTN/Airtel):")

#Handling MTN Transactions
if operator=="1":
    print("MTN selected")
    print(f"Your current balance is " , {mtn_balance})

#user input for the transaction
transaction_type=input("Enter transaction type (send/withdraw):")

# send transaction
if transaction_type=="send":
    amount= int(input("Enter the amount  to send: "))
    charge = send_charges(amount, send_charge_mtn)
    tax = tax_rate*amount
    total = amount + charge + tax
    print(f"Sending {amount} with charge {charge} and tax {tax} = {total}")
    mtn_balance -=total

#Handling withdraw transaction
elif transaction_type=="withdraw":
    amount = float(input("Enter amount to withdraw: "))
    charge = withdraw_charge(amount, withdraw_charge_mtn) 
    tax = tax_rate*amount
    total = amount + amount + tax
    print(f"Withdrawing {amount} with charge {charge} and  a tax of {tax} = {total}")
    mtn_balance


#Handling Airtel Transactions
elif operator == "2":
    print("Airtel selected")
    print(f"Your current balance is {airtel_balance}")

#getting user input for the transaction type (send/withdraw)
transaction_type= input ("Enter transaction type(send/withdraw): ")

#Handling send transaction
if transaction_type=="Send":
    amount= int(input("Enter amount to send: "))
    charge = send_charges(amount, send_charge_airtel)
    tax = tax_rate(amount)
    total= amount + charge + tax
    print(f"Sending {amount} with charge {charge} and tax {tax} = {total}")
    airtel_balance-=total

#Handling withdraw transaction 
elif transaction_type == "withdraw":
    amount = float(input("Enter amount to withdraw: "))
    charge = withdraw_charge(amount,withdraw_charge_airtel)
    tax = tax_rate*amount
    total= amount + charge + tax
    print(f"Withdrawing {amount} with charge {charge} and tax {tax} = {total}")
    airtel_balance-=total

#call the function
main()


