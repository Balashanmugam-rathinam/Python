# Define a global variable named 'glo' and assign it the value "bala"
glo = "bala"

# Define the main function
def main():
    global glo  # Declare that we will use the global variable 'glo' inside this function
    say("hello")  # Call the 'say' function with the word "hello"
    say("Hi")      # Call the 'say' function with the word "Hi"

# Define the 'say' function that takes one parameter 'Pharse'
def say(Pharse):
    # Print the phrase combined with the global variable 'glo'
    print(Pharse + " " + glo)

# Call the main function to start the program
main()
