file = open('C:\Users\ashif\Desktop\AI_Projects\python\7_exception_handling/main.py' , "r")

print(file.read())

"""
r->read (file must be exist)
w->write (creates file or override)
a->append (add content at the end)
x->   (creates a new file fails if exist)
"""


file.close()
