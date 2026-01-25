#!! loops

#! for loop
# range(start, stop , step) --> default range(0 , stop , 1)
print("For Loop")
for i in range(100 , 1 , -1):
    print(f"value of i is {i}")

r = int(input("Enter a range to check if 5's multiple is exist or not --> "))
#! for else loop
for i in range(5):
    if i % 5 == 0 :
        print(f"Multiple of 5 exist from 0 to {r}")
        break
else:
    print(f"any multiple of 5 not exist from 0 to {r}")

#! while loop
i = 1
print("\n\nWhile loop")
while i < 100:
    print(f"value of i is {i}")
    i+=1

your_name="Ash"
# index access
for i in range(len(your_name)):
    print(your_name[i])

# direct access
for i in your_name:
    print(i)


