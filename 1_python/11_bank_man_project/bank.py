import json
from pathlib import Path
import random
import string

class Bank:
    data = []
    database = "data.json"
    try:
        if Path(database).exists() :
            with open(database , "r") as fs :
                data = json.loads(fs.read())
        else:
            print("Database not exist")
    except Exception as err:
        print(f"An error occured as {err}")
        
    @classmethod
    def __update_database(cls):
        with open(cls.database , "w") as fs :
            fs.write(json.dumps(cls.data))

    @classmethod
    def __generate_account(cls):
        alpha = random.choices(string.ascii_letters , k=3)
        num = random.choices(string.digits , k=3)
        spchr = random.choices("~@#$%&*" , k=1)
        id = alpha + num + spchr
        random.shuffle(id)
        return "".join(id)

    def create_account(self):
        print("Creating an Account")
        info = {
            "name": input("Enter your name :- "),
            "email": input("Enter your email :- "),
            "age": int(input("Enter your age :- ")),
            "pin": int(input("Enter pin of 4 numbers :- ")),
            "account": Bank.__generate_account(),
            "balance": 0
        }
        if info["age"] < 18 or len(str(info["pin"])) != 4 :
            print("Sorry , You can't create an account")
        else:
            Bank.data.append(info)
            Bank.__update_database()
            print("Account Created Success")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Note your account details to access later\n\n")

    def update_account(self):
        accNo = input("Enter your account number :- ")
        pin = int(input("Enter your pin :- "))
        userAcc = [i for i in Bank.data if i["account"] == accNo and i["pin"] == pin]
        if not userAcc :
            print("Cant find your account")
        else:
            userAcc=userAcc[0]
            print("Your current details are --> ")
            for i in userAcc:
                print(f"{i} : {userAcc[i]}")
            print("Input the fields if want to change or leaves it ")
            new_info = {
                "name": input("Enter your name :- "),
                "email":input("Enter your email :- "),
                "pin":input("Enter pin of 4 numbers :- "),
            }
            if new_info["pin"] == "":
                new_info["pin"]=userAcc["pin"]
            elif len(new_info["pin"]) != 4 :
                print("Account update failed due to invalid pin")
                return 
            else:
                new_info["pin"] = int(new_info["pin"])
            if new_info["name"] == "":
                new_info["name"]=userAcc["name"]
            if new_info["email"] == "":
                new_info["email"]=userAcc["email"]

            for i in new_info:
                if new_info[i] == userAcc[i]:
                    continue
                else:
                    userAcc[i] = new_info[i]
            
            Bank.__update_database()
            print("Account update success")

    def check_account(self):
        accNo = input("Enter your account number :- ")
        pin = int(input("Enter your pin :- "))
        userAcc = [i for i in Bank.data if i["account"] == accNo and i["pin"] == pin]
        if not userAcc :
            print("Cant find your account")
        else:
            userAcc = userAcc[0]
            print("Your details are --> ")
            for i in userAcc:
                print(f"{i} : {userAcc[i]}")


    def delete_account(self):
        accNo = input("Enter your account number :- ")
        pin = int(input("Enter your pin :- "))
        userAcc = [i for i in Bank.data if i["account"] == accNo and i["pin"] == pin]
        if not userAcc :
            print("Cant find your account")
        else:
            userAcc=userAcc[0]
            i = Bank.data.index(userAcc)
            confirm = input("Enter Y to confirm delete :- ")
            if confirm == "Y":
                Bank.data.pop(i)
                Bank.__update_database()
                print("Account deleted Success")

    def deposit(self):
        accNo = input("Enter your account number :- ")
        pin = int(input("Enter your pin :- "))
        userAcc = [i for i in Bank.data if i["account"] == accNo and i["pin"] == pin]
        if not userAcc :
            print("Cant find your account")
        else:
            userAcc=userAcc[0]
            amount = int(input("Enter amount to deposit :- "))
            if amount > 10000 or amount <= 0 :
                print("Amount should be in between 1 to 10000")
            else:
                userAcc["balance"]+=amount
                Bank.__update_database()
                print(f"Amount deposited , total balance {userAcc["balance"]} ")


    def withdraw(self):
        accNo = input("Enter your account number :- ")
        pin = int(input("Enter your pin :- "))
        userAcc = [i for i in Bank.data if i["account"] == accNo and i["pin"] == pin]
        if not userAcc :
            print("Cant find your account")
        else:
            userAcc=userAcc[0]
            amount = int(input("Enter amount to withdraw :- "))
            if amount > 10000 or amount <= 0 :
                print("Amount should be in between 1 to 10000")
            else:
                userAcc["balance"]-=amount
                Bank.__update_database()
                print(f"Amount withdrawed , total balance {userAcc["balance"]} ")


bank = Bank()

while True:
    print("__________________________")
    print("|        Bank Menu       |")
    print("| 1.Create Account       |")
    print("| 2.Update Account       |")
    print("| 3.Check Account        |")
    print("| 4.Delete Account       |")
    print("| 5.Deposit Amount       |")
    print("| 6.Withdraw Amount      |")
    print("| 7.Exit                 |")
    print("__________________________")
    choice = int(input("Enter your Choice -> "))
    if choice == 1 :
        bank.create_account()
    if choice == 2 :
        bank.update_account()
    if choice == 3 :
        bank.check_account()
    if choice == 4 :
        bank.delete_account()
    if choice == 5 :
        bank.deposit()
    if choice == 6 :
        bank.withdraw()
    if choice == 7 :
        break