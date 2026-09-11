weight = float(input("Enter your weight:"))
height = float(input("Enter your height:"))

bmi = weight / height ** 2 

if bmi < 18.5:
    category = 'under weight'
elif bmi < 25:
    category = "You are in normal weight"
elif bmi < 30:
   category = "your are over weight"
else:
    category = 'obese'
    
print(f"BMI = {bmi:.2f} ({category})")