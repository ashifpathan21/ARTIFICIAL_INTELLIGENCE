#! module (file) import
# import 2_comprehension  # Invalid module name, commented out
import module
# from module import add 


#! Package (folder) import
# import 9_oops  # Invalid module name, commented out
import package
from package import hello

hello.hello()

l = [1 ,2 , 4 , 5, 6, 7, 8]

doubled = list(map(lambda x : x*2 , l))
print(doubled)

evens = list(filter(lambda x : x%2 == 0 , l))
print(evens)


