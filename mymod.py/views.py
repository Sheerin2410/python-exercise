all_laptops = {
    "dell" :65000,
    "hp":45000,
    "lenovo":70000,
}

all_mobile = {
    "samsung":30000,
    "mi":14000


}
customer_cart={}

def viewlaptop():
    print("\n LAPTOP LIST\n")
    for k,v in all_laptops.items():
        print(f"{k}={v}")

def viewmobile():
    print("\n MOBILE LIST\n")
    for k,v in all_mobile.items():
        print(f"{k}={v}")

def purchaselaptop(laptop_name,qty):
    if laptop_name in all_laptops:
        price=all_laptops[laptop_name]
        total_price = qty*price
        print("total price=",total_price)
        return total_price
def addtocart(customername,product,productname,qty,price):
    specifications={}
    if customername not in customer_cart:
        specifications["product_name"] = productname
        specifications["qty"] = qty
        specifications["total_price"] = price
        customer_cart[customername] = specifications
        print(customer_cart)




