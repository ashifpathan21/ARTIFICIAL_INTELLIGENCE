#! List
array_list = [1 ,2] # mutable
heterogeneous_list = [1 , 1.5 , True , "ash"] # heterogeneous
# methods
array_list.append(4) # insert at last
print(array_list)
array_list.insert(1 , 2) # insert at a position
print(array_list)
array_list.extend([3 , 5 ,7]) # insert another list
print(array_list) 
array_list.remove(2) # remove the first occurence of an element
print(array_list)
element = array_list.pop() # remove and get last element
print(array_list)
print(element)
count_of_5 = array_list.count(5) # count occurence of an element
print(count_of_5)
index_of_5 = array_list.index(5) # return index of an element
array_list.sort() # sort a list
print(array_list)
reverse_list = array_list.copy().reverse()  # copy (shallow) & reverse a list
print(reverse_list)

a = array_list # deep copy

