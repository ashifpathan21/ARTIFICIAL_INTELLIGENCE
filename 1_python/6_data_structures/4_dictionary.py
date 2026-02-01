#! Dictionary (hashmap)
a = {
    1:"Hello",
    2:"World"
}

"""
key-> unique , immutable
heterogeneous
value-> can be same , mutable
"""
print(f"{a[1]} {a[2]}")
a[1]="Namaste"  # Updating
a[3]=" , Welcome" # Creating

for i in a:
    print(f"Key is {i} value is {a[i]}")

b = a # Deep copy
b = a.copy() # Shallow copy

# Methods
help(dict)
isExist = a.get(20)
print(isExist) # None

