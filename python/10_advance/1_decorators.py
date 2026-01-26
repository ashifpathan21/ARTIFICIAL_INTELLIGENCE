# is just a function that modifies another function without changing its code 

class Animal:
    @property
    def hello(self):
        print("Hello i am an animal")


obj =Animal()
obj.hello # no need of this obj.hello()

# creating a decorator

def decorate(fun):
    def wrappper(*args , **kargs): 
        """
         args -> arguments is tupple ,
         kargs -> keyword arguments is type of map/dictionary for positional argument access by kargs[i] where i is the argument name
         also wrapper(name)
        """
        print("Welcome")
        fun(*args , **kargs)
        print("Thanks You")
    return wrappper


@decorate
def printMyName(name):
        print(f"Hy , I am {name}")


printMyName("Ashif Pathan")