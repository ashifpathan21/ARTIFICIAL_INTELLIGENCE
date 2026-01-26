#! Set ( mutable , unordered )
s = {} # if empty --> dictionary
s = {1 , 3 , 2 , 4 , 3 } # No duplicate value be added 
# sorted for numbers because hash of numbers represent itself but in case of other it can be anywhere depends on the hash
print(s) # {1 , 2 , 3 , 4 }


# set uses hashing
b = hash((1, 3 ,4))
print(b)
a = hash("Hello")
print(a)
# only immutable objects can be stored in a set

# methods
s.add(0)
s.remove(3) # raise an error if not found 
s.discard(3) # not raise any error
el = s.pop() # remove random element
s.clear() # to empty a set


set_1 = {2 , 3 , 4 , 4 ,5 ,6}
set_2 = {1, 2, 3, 5 , 7 , 9 , 0}


#! Union (joins both sets)
set_union = set_1.union(set_2)
print(set_union)
# or
set_union = set_1 | set_2 
print(set_union)

#! Intersection (give common part)
set_intersection = set_1.intersection(set_2)
print(set_intersection)
# or
set_intersection = set_1 & set_2
print(set_intersection)

set_difference = set_1.difference(set_2) # part of set_1 that is not in set_2 --> {4 , 6}
print(set_difference)
# or
set_difference = set_2 - set_1 # part of set_2 that is not in set_1 --> {0 ,  1 , 7 , 9}
print(set_difference)

set_semetric_diff = set_1.symmetric_difference(set_2) # give (A U B) - (A n B)
print(set_semetric_diff)
set_semetric_diff = set_1 ^ set_2
print(set_semetric_diff)