principle_amount = float(input("Enter the principle amount:"))
rate_of_interest_per_year = float(input("Enter the rate of interest(%year):"))
total_years = float(input("Enter the number of year:"))

simple_interest = principle_amount * rate_of_interest_per_year * total_years / 100

print(f"simple interest:{simple_interest}")