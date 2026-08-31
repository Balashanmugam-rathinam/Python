num = int(input("Enter the number:"))
count =  0
n = num 
while n > 0:
    count = count + 1
    n = n // 10
print(num,"has",count,"digits")