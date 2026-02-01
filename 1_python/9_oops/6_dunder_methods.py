# methods that starts and end with __ 
# automatically get called when we perform certain action on an object

class Animal:
    def __init__(self , age):
        self.age=age
        print("Animal initiated")
    
    def __str__(self):
        return f"Animal with age -> {self.age}"
    def __add__(self , other):
        print("Adding")
        return Animal(self.age + other.age)


an1 =Animal(10)
an2 =Animal(20)
print(an1) # Animal with age -> 10
an3 = an1+an2 # Adding
print(an3)