# # map() applies int() to every piece produced by
# split()
a,b,c = map(int,input("enter the numbers:").split())
avg = (a + b + c) / 3
print(f"{avg:.2f}")

