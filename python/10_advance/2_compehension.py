num = int(input("Enter no to check even or odd :-- "))
# ternary operator
print("even") if num%2 == 0 else print("Odd")

# dict , list , set compehensions
evens = [i for i in range(num) if i%2 == 0]
odds = [i for i in range(num) if i%2 != 0]
squares = {i:i**2 for i in range(1 , num+1)}
print(f"Even till now => {evens}")
print(f"Odd till now => {odds}")
print(f"Squares till now =>")
for i in squares:
    print(f"{i} : {squares[i]}")


# lambda function
add = lambda a, b : a+b

print(add(3 , 4))