from math import factorial


num = int(input("enter number : "))
factorial=1

if num<0:
    print("factorial of nagative number does not exist")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num=1):
        factorial=factorial*i
        print("The factorial of",num,"is",factorial)    
