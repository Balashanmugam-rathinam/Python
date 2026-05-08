# age = int(input("Enter your age:"))
# driving_license = input("Do you have Driving-license ('yes')or('no'):")

# if age >= 18 and driving_license.lower() == 'yes' :
#     print("you can drive vehical")
# elif age >= 18 and driving_license.lower() == 'no':
#     print("you cant drive vehical")
# else:
#     print("come when you 18")    
    
# if age >= 18:
#     if driving_license.lower() == "yes":
#         print("you can drive")
#     else:
#         print("go take a license")
# else:
#     print("come when you 18, tata kiddo")

recharge = int(input("Enter the amount:"))
days = input("Enter the day:")
membership = input("Do you have membership:")

if (recharge >= 1000 and days in['sat','sum']) or membership == 'yes':
    print("You have 20% Discount")
else:
    print("No Discount")