# hiding details - misaccess , change , access modify , binding attribute with method

class Account :
    # public
    name = "SBI"
    # protected - only naming convention but it can be access as public
    _IFSC = "1234"
    # private - can't access
    __amount=12



class Employee :
    def __init__(self, name ,age , salary):
        self.name = name # Public
        self._age=age # Protected
        self.__salary=salary # Private

    def show(self):
        print(f"Employee: {self.name} has age {self._age} & salary {self.__salary}")


emp1=Employee("Ash" , 20, 10000)
emp1.show()
emp1._age = 30 #changed 
emp1.__salary = 20000 # not changed
emp1.show()


