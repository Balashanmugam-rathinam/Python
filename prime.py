#prime number
num = int(input("Enter the number:"))
if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print("The given number is not prime")
            break
    else:
        print("the number is prime")
else:
    print("The given number is not prime")