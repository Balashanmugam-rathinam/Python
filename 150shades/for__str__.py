class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} year old"
    
dog1 = Dog("buddy",4)
dog2 = Dog("cuddy",5)

print(dog1)
print(dog2)
        