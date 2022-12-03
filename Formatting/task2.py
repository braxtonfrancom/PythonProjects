# Braxton Francom
# CS1400 - LW2
# Assignment 4

table = ""

# Prompt user for employee's name
employeeName = (input("Enter employee's name: "))

# Prompt user for number of hours worked in one week
numHours = eval(input("Enter number of hours worked in a week: "))

# Prompt user for hourly pay rate
payRate = eval(input("Enter hourly pay rate: "))

# Prompt user for federal tax withheld
fedTax = eval(input("Enter federal tax withholding rate (ex. 0.12): "))

# Prompt user for state tax withheld
stateTax = eval(input("Enter state tax withholding rate (ex. 0.06): "))

# New line
table += "\n"

# Display <employeeName>'s PAY INFORMATION
table += (str(format(employeeName.upper() + " PAY INFORMATION", "^42")))

# New line
table += "\n" + "\n"

# Display "Pay"
table += (format("Pay", "^42"))

# New line
table += "\n"

# Display hours worked
table += (format("Hours Worked:", ">30") + str(format(numHours, ">12.0f")))

# New line
table += "\n"

# Display pay rate
table += (format("Pay Rate: " + "$", ">32") + str(format(payRate, ">10.2f")))

# Calculate gross pay
grossPay = numHours * payRate

# New line
table += "\n"

# Display gross pay
table += (format("Gross Pay:" + " $", ">32") + str(format(grossPay, ">10.2f")))

# New line
table += "\n" + "\n"

# Display Deductions
table += (format("Deductions", "^42" ))

# New line
table += "\n"

# Calculate federal withholding total
fedTotal = fedTax * grossPay

# Reformat fedTax to display as a percent
fedTax *= 100

# Display Federal withholding total
table += (format("Federal Withholding " + "(" + str(format(fedTax, "2.1f")) + "%):", ">30") + " $" + str(format(fedTotal, ">10.2f")))

# New line
table += "\n"

# Calculate State withholding total
stateTotal = stateTax * grossPay

# Reformat stateTax to display as a percent
stateTax *= 100

# Display State withholding total
table += (format("State withholding " + "(" + str(format(stateTax, "2.1f")) + "%):", ">30") + " $" + str(format(stateTotal, ">10.2f")))

# New line
table += "\n"

# Calculate total deduction
totalDeduction = fedTotal + stateTotal

# Display total deduction
table += (format("Total Deduction:", ">30") + " $" + str(format(totalDeduction, ">10.2f")))

# New line
table += "\n"

# Calculate Net Pay
netPay = grossPay - totalDeduction

# Display Net Pay
table += ("\n" + format("Net Pay:", ">30") + " $" + str(format(netPay, ">10.2f")))

print(table)