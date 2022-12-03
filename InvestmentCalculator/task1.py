# Braxton Francom
# CS1400 - LW2
# Assignment 3 Task1

# Enter investment amount
investmentAmount = eval(input("Enter investment amount: "))

# Enter monthly payment amount
monthlyPaymentAmount = eval(input("Enter monthly payment amount: "))

# Enter annual interest rate
annualInterestRate = eval(input("Enter annual interest rate: "))

#Calculate monthly interest rate (as a decimal)
monthlyInterestRate = annualInterestRate / 1200

# Enter number of years
numberOfYears = eval(input("Enter number of years: "))
numberOfMonths = numberOfYears * 12

# Calculate future value
futureValue = investmentAmount * (1 + monthlyInterestRate) ** (numberOfMonths) + monthlyPaymentAmount * (((1 + monthlyInterestRate) ** (numberOfMonths) - 1) / monthlyInterestRate) * (1 + monthlyInterestRate)

# Display future value
print("The future value is $"+ str(round(futureValue, 2)))

