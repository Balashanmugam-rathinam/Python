age = int(input("Enter your age:"))
driving_license = input("Do you have Driving-license ('yes')or('no'):")

# if age >= 18 and driving_license.lower() == 'yes' :
#     print("you can drive vehical")
# elif age >= 18 and driving_license.lower() == 'no':
#     print("you cant drive vehical")
# else:
#     print("come when you 18")    
    
if age >= 18:
    if driving_license.lower() == "yes":
        print("you can drive")
    else:
        print("go take a license")
else:
    print("come when you 18, tata kiddo")