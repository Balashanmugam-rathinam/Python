def greet(input):
    if "hello" in input:
        return "hello, there"
    else:
        return "what you mean?"

greeting = greet(input("Enter the value:"))
print(greeting + " bala")
