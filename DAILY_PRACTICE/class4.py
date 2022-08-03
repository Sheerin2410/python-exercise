# EXCEPTION : 
"""which disturb the normal flow of the program

 To handle such kind of exception is caled as EXCEPTION HANDLING..
USING OF TRY AND EXCEPT WE CAN HANDLE EXCEPTION.""""

# SYNTAX:
"""
try :
       code
except :
       statement
"""
"""
try:
    print(a)
except:
    print("Invalid input")
"""


#NUBER Division

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

"""
TRY : which contain rrror block

EXCEPT: which call when error occurs

FINALLY : it always execute exception call or not

ELSE: it always execute when there is no exception
"""