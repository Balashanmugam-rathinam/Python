p = float(input("Enter your principle:"))
r = float(input("Enter your rate (% per year):"))
t = float(input("Enter time or holding period(How many year)"))

amount = p * (1 + r / 100) ** t
cp = amount - p

print(f"Final amount : {amount:.2f}")
print(f"compound interest:{cp:.2f}")