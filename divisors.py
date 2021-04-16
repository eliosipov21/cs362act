def printDivs(a):
    for i in range(1,a+1):
        if(a % i == 0):
            print(i)

a = int(input("enter a number \n") )
print("divisors : ")
printDivs(a) 