num = int(input("Enter a number: "))
total = 0
n = num
while n > 0:
    total += n % 10 # n % 10 gives the lastdigit
    n //= 10 # n = 10 removes thelast digit
print("Sum of digits of", num, "is", total)