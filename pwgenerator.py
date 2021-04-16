import string 
import random 
def generate(a):
    str = ""
    for i in range(a):
        str += random.choice(string.ascii_letters)
    print(str)


a = int(input("Enter a number: "))
generate(a)