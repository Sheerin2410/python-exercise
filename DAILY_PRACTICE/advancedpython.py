"""
class : 
    is a collection of data member and member function which contains data member 
and member function in a single entity.

object:
    object is a variable of class.

    using of object we can access properties of class.

SYNTAX:
     
class classname:
    properties

obj = classname()

"""
class Sample:
    num1 = 10
    num2 = 20

obj = Sample()
print(obj.num1)
print(obj.num2)

# SELF : which represents current class properties

class Student:
    def display(self,fname,lname):
        print("hello")
        print("fname = ",fname)
        print("lname = ",lname)

obj = Student()
obj.display("ABC","XYZ")

# FACTORIAL PROGRAM USING OBJECT 

class Practical:
    def findfactorial(self,num):
        f = 1
        for i in range(1,num+1):
           f*=i
        print("Factorial =",f)

obj = Practical()
num = int(input("Enter a Number : "))
obj.findfactorial(num)

# Difference between method and fuctions:

"""
1) function :
     which is declare outside the class
    - functions are independent

    SYNTAX:
       def myfun():
            statement

2) method :
     which is declare inside the class 
    - methods are dependent on class - object

    SYNTAX:
       def myfun():
            statement

"""

# ENCAPSULATION 

"""
Encapsulation : 
     data member and member function contain in single entity is called as encapsulation.

     example : class
"""

# getname,setname,setsubject,getsubject

class Student:
    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

    def setSubject(self,subject):
        self.subject = subject

    def getSubject(self):
        return self.subject

obj = Student()
obj.setName("Sheerin")
obj.setSubject("Python")

print("name = ",obj.getName())
print("subject = ",obj.getSubject())