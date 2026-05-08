# Variable simply containers for some value that can change over time
def get_guess():
    guess = 10 # the guess is a variable, it contain value of 10.
    return guess
print(get_guess())

def get_guess1():
    guess = int(input("Enter the guess:")) # the guess is a variable, it contain value of 10.
    if guess == 50:
        print("correct")
    else:
        print("incorrect")
        return 
get_guess1()


