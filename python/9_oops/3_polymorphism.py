class Engine:
    def __init__(self):
        print("Engine build")
    def start(self):
        print("Engine started")

class Car(Engine):
    def __init__(self):
        super().__init__()
        print("Car build")

    # Method overriding - no overloading exist here 
    def start(self):
        print("Car started")

eng  = Engine()
eng.start()
bmw = Car()
bmw.start()


#! Duck typing
"""
same function name without inheritance but definition can be different
"""



    