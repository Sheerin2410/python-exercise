try:
    num1 = int(input("Enter a number"))
    num2 = int(input("Enter a number"))
    ans=num1/num2
    
except ZeroDivisionError:
    print("number is not devide by zero")
except:
    print("Invalid Input")
else:
    print(ans)
finally:
    print("THANKYOU FOR USING THIS APP")