#---------------------------
# SINGLE LEVEL INHERITANCE #
#---------------------------

class Parent:
    def display(self):
        print("hello parent class method called")

class Child(Parent):
    def child_dispaly(self):
        print("hello child class method called")

obj = Child()
obj.display()
obj.child_dispaly()

#---------------------------
# MULTIPLE INHERITANCE #
#---------------------------

class A:
    def displayA(self):
        print("A class display")
class B(A):
    def displayB(self):
        print("B class display")
class C(B):
    def displayC(self):
        print("C class display")

obj = C()
obj.displayA()
obj.displayB()
obj.displayC()

#---------------------------
# MULTI - LEVEL INHERITANCE #
#---------------------------

class A():
    def displayA(self):
        print("A class display")
class B(A):
    def displayB(self):
        print("B class display")
class C(A):
    def displayC(self):
        print("C class display")

obj1 = B()
obj2 = C()
obj.displayA()
obj1.displayB()
obj2.displayC()




