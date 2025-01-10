# A calculator
Operator=input("Enter the operator(+ - * /) : ")
num1=float(input("Enter the 1st number :"))
num2=float(input("Enter the 2nd number :"))
if Operator== "+":
    result=num1 +num2
    print(round(result,3))
elif Operator=="-":
    result=num1-num2
    print(round(result,3))
elif Operator=="*":

    result=num1*num2
    print(round(result,3))
elif Operator=="/":
    if num2 ==0:
     raise ValueError("Cannot divide by zero")
    result=num1/num2
    print(round(result,3))


   