#! Class - blueprint
class Factory :  
    #attributes
    count=0 # class attribute
    # instance method takes (self) as a parameter 
    def hello(self):
        print(f"Hello , I am a {self.name}")
    
    # constructor
    def __init__(self , name):
        self.name=name # instance attribute
        self.increase_count()
        print("Factory initialized")

    @classmethod
    def increase_count(cls):
        cls.count+=1
    
    def show_count(cls):
        print(f"{cls.count} factories has been created !")

    def decrease_count(cls):
        cls.count-=1
    
    @staticmethod # as a normal utility function
    def start():
        print("Starting")

#! Object - instance
toyata = Factory("Toyata")
toyata.hello()
bmw = Factory("BMW")
bmw.hello()
toyata.show_count()
