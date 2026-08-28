total = int(input("Enter seconds: "))
hours = total // 3600 # whole hours
minutes = (total % 3600) // 60 # leftover minutes
seconds = total % 60 # leftover seconds
print(f"{hours} hour(s) {minutes} minute(s) {seconds} second(s)")
