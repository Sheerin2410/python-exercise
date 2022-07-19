from views import*

name = input("Enter your name : ")
menu = """
      MENU

      1)LAPTOP
      2)MOBILE
"""
print(menu)

choice = int(input("Enter Your choice :"))
if choice==1:
    viewlaptop()
    laptop_name =input("Enter laptop name which you want to purchase :")
    qty =int(input("Enter no. of quentity :"))
    total_price = purchaselaptop(laptop_name,qty)
    choice=input("do you want to purchase it press 'y'for yes:")
    if choice=='y' or choice=='yes':
        addtocart(name,"laptop",laptop_name,qty,total_price)

elif choice==2:

    viewmobile()

else:
    print("Invalid Input")