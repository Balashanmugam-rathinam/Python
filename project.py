# #Trivia Game
# #List of questions
# #store the answers

# #randomly pick questions
# #ask the questions
# #see if they are correct
# #keep trace of the score
# #tell the user their score

# questions ={
#     "what is the keyword to define a function is python?":"def",
#     "Which datatype is used to store True or False values in python":"boolean",
#     "what is the correct extension for python file":".py"
# }
# print(type("python"))
# print(5==5)
# print(len('Python'))
x = 1
# def fun():
#     global x
#     x = x + 1
# fun()
# print(x)
from multiprocessing import Pool

def square(x):
    return x * x
if __name__ == "__main__":
    with Pool(2) as pool:
        result = pool.map(square,[2,3,4])
        print(result)