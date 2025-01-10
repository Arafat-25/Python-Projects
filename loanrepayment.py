# Loan Repayment Calculator

# Get user input
principal = float(input("Enter the loan amount: "))
interest_rate = float(input("Enter the interest rate (in %): "))
loan_term = int(input("Enter the loan term (in years): "))

# Calculate monthly interest rate
monthly_interest_rate = interest_rate / 1200

# Calculate loan duration in months
loan_duration_months = loan_term * 12

# Calculate monthly payment
monthly_payment = principal * monthly_interest_rate * (1 + monthly_interest_rate) ** loan_duration_months / ((1 + monthly_interest_rate) ** loan_duration_months - 1)

# Print results
print("Monthly payment: {:.2f}".format(monthly_payment))
print("Total interest paid: {:.2f}".format(monthly_payment * loan_duration_months - principal))
print("Total amount paid: {:.2f}".format(monthly_payment * loan_duration_months))