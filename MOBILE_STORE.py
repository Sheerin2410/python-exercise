Mobile_store = {}
menu = """
         MENU
PRESS 1 FOR PRODUCT MANAGER
PRESS 2 FOR CUSTOMER
"""
Status=True
while Status:
  Specifications = {}
  print(menu)
  role=int(input("Choose your role 1/2 :"))
  if role==1:
    print("PRODUCT MANAGER")
    product_name=input("Enter Product Name :")
    model_no=input("Enter Model No :")
    color=input("Enter Color of Model :")
    qty=int(input("Enter quantity of product :"))
    price=int(input("Enter Price :"))

    Specifications["model"] = model_no
    Specifications["color"] = color
    Specifications["qty"] = qty
    Specifications["price"] = price

    Mobile_store[product_name] = Specifications
    print(Mobile_store)

  elif role==2:
    print("CUSTOMER")

  else:
    print("Invalid Input")
    
    choice = input("Do You want to continue ? Press 'y' for YES and press 'n' for NO")

  if choice == 'n' or choice =='no' :

    Status=False



    for k in Mobile_store.keys():

     print("--------------------------")
     print(f"PRODUCT : {k}")  
     print("MODEL :"+Mobile_store[k]["model"])
     print("COLOR :"+Mobile_store[k]["color"])
     print("QTY :"+Mobile_store[k]["qty"])
     print("PRICE :"+Mobile_store[k]["price"])