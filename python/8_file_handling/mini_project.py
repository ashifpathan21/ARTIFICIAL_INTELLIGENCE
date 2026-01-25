from pathlib import Path
import os 

# Show all file
def showFilesAndFolders():
    p = Path('')
    items = p.rglob("*")
    for i , items in enumerate(items):
        print(f"{i+1} : {items}")

# create a file 
def createFile():
    try:
        showFilesAndFolders()
        name = input("Enter file name to create :- ")
        p  = Path(name)
        if not p.exists():
            with open(p , "w") as fs:
                data = input("Enter Content of the file :- ")
                fs.write(data)
            print("File created Successfully")
        else:
            print("File already exist or invalid file name")
    except Exception as err:
        print(f"An error occured {err}")


# update a file 
def updateFile():
    try:
        showFilesAndFolders()
        name = input("Enter file name :- ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("-------------------------")
            print("|    Update options     |")
            print("| 1.Change file name    |")
            print("| 2.Change file data    |")
            print("| 3.Add some data       |")
            print("-------------------------")
            choice = int(input("Enter your choice -> "))
            if(choice == 1):
                new_name= input("Enter new name :- ")
                new_p = Path(new_name)
                p.rename(new_p)
                print("Name is changed")
            if(choice == 2):
                with open(p , "w") as fs:
                    data = input("Enter data to override content :- ")
                    fs.write(data)
                print("File content changed")
            if(choice == 3):
                with open(p , "a") as fs:
                    data = input("Enter data to add :- ")
                    fs.write(" " + data)
                print("Data appended to the file")
        else:
            print("File not exist")
    except Exception as err:
        print(f"An error occured {err}")

def readFile():
    try:
        showFilesAndFolders()
        name = input("Enter file name to read :- ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p , "r") as fs :
                print(f"Content of file:{name} is \n\n")
                print(fs.read())
                print("\n\n\n Ended")
        else:
            print("File doesn't exist")
    except Exception as err :
        print(f"An error occured {err}")

def deleteFile():
    try:
        showFilesAndFolders()
        name = input("Enter file name to delete :- ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("File Deleted Success")
        else:
            print("File doesn't exist")
    except Exception as err :
        print(f"An error occured {err}")


while True :
    print("__________________________")
    print("|        File Menu       |")
    print("| 1.Create file          |")
    print("| 2.Update file          |")
    print("| 3.Read file            |")
    print("| 4.Delete file          |")
    print("| 5.Exit                 |")
    print("__________________________")
    choice = int(input("Enter your Choice -> "))
    if choice == 1 :
        createFile()
    if choice == 2 :
        updateFile()
    if choice == 3 :
        readFile()
    if choice == 4 :
        deleteFile()
    if choice == 5 :
        break