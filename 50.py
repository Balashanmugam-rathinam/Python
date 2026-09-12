income = float(input("Enter annual income:"))

tax = 0.0
if income > 1000000:
    tax = tax + (income - 1000000) * 0.3
    income = 1000000

if income > 500000:
    tax = tax + (income - 500000) * 0.2
    income = 500000
    
if income > 250000:
    tax = tax + (income - 250000) * 0.05
    income = 250000
    
print(f"Income:{income}\ntax:{tax}")