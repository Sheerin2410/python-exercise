data ="""
          Welcome to Amazing Pizza and Pasta Pizzeria

press 1 : Order menu
press 2 : Exit

"""
menu="""             1 large pizza = 10.99 AUD 

                     2 large Pizzas = 20.99 AUD 

                     3 Large Pizzas = 29.99 AUD

                     ***Buy 4 or more pizza and get 1.5lt of soft drink free***


                    1 large pasta = 9.5 AUD 

                    2 large pastas = 17.00 AUD 

                    3 large pastas = 27.50 AUD

                    ***Buy 4 or more pastas and get 2 bruschetta free.***

                    ***Buy 4 or more pizzas and pastas and get 2 chocco brownies ice cream free."""

print(data)
amount=0

class pizzeria:
        name = input("Enter Your Name :")
        def setName(self,name):
        
            self.name = name

        def getName(self):
         return self.name
obj = pizzeria()
print("WELCOME ",obj.getName())

choice=int(input("Enter Your Choice here : "))
if choice==1:
                print(menu)                             
elif choice==2:
     exit()

def pizza():
    choice = int(input("Enter number of pizza order you want :"))
    if choice>=4:
        print("""*** Congratulations !! 1.5lt softdrink free *** """) 
        
pizza_name=input("Enter the name of pizza you want : ")

if pizza_name=='pizza1':
     price=10.99  
     print("1 large pizza = ",price,"AUD")
     amount=choice*price
elif pizza_name=='pizza':
    price=20.99
    print("2 large Pizzas = ",price,"AUD")
    amount=choice*price
elif pizza_name=='pizza3':
    price=30.99
    print("3 Large Pizzas = ",price,"AUD")
    amount=choice*price

else:
        print("your pasta order amount is",choice)

obj = pizza()
def pasta():
    choice = int(input("Enter number of pasta order you want :"))
    if choice>=6:
        print("""
        *** Congratulations !! get 2 bruschetta free *** 

		*** Congratulations !! get 2 chocco brownies ice cream free *** """) 
        
pasta_name=input("Enter the name of pasta you want : ")

if pasta_name=='pasta1':
     price=9.5  
     print("1 large pasta = ",price,"AUD")
     amount=choice*price
elif pasta_name=='pasta2':
    price=17.00
    print("2 large pastas = ",price,"AUD")
    amount=choice*price
elif pasta_name=='pasta3':
    price=27.50
    print("3 large pastas = ",price,"AUD")
    amount=choice*price

else:
        print("your pasta order amount is",choice)

obj = pasta()
#def total_cost():
   # amount=choice*price
    #print("total_price is :",amount)
#obj=total_cost()



