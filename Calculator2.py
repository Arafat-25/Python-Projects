def add(x,y):
    return(x+y)
def subtraction(x,y):
    return(x-y)
def divide(x,y):
    if y==0:
        raise ValueError("Cannot divide by Zero!")
    return(x/y)
def mulitply(x,y):
    return(x*y)

while True:
    print("1. Add")
    print("2.Subtract")
    print("3.Divide")
    print("4.Multiply")
    print("5.Quit")
    choice = input("Choose an option:")

    if choice == "5":
        break

    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))

    if choice=="1":
        result= add(num1, num2)
    elif choice=="2":
        result= subtraction(num1, num2)
    elif choice=="3":
        result=divide(num1, num2)
    elif choice=="4":
        result=mulitply(num1, num2)
    print("Result :",result)