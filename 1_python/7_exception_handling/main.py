r = int(input("Enter Number for dividing 1 : "))
# try , except , else , finally , raise
try:
    print(1/r) # zero division error
    # print("1"/r) 
except ZeroDivisionError:
    print("Dividing with 0 is not supported")
except Exception as err:
    print("Something went wrong")
    # raise RuntimeError("Something went wrong")
else:
    print("Division done")
finally:
    print("Good Bye")

