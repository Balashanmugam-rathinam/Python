total = int(input("Enter the secound:"))
hour = total // 3600
minute= (total % 3600) // 60
second = total % 60
print(f"hour:{hour} minutes{minute}  second{second}")
