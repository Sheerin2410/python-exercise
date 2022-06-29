orderList = []
option = 'y'

menu = [
    ['Dabeli', 20],
    ['Butter Dabeli', 30],
    ['Puff', 30],
    ['Puff grilled', 40],
    ['Vadapav', 20],
    ['Butter Vadapav', 30],
    ['Spread', 25],
]

print("\n\n\t****** MENU ******")
for item in menu:
    print(f"\t{item[0]} -> {item[1]}")


while option == 'y':
    print("\n\tPress-1 for add item")
    print("\tPress-2 for remove item")
    print("\tPress-3 for display items")
    print("\tPress-4 for checkout")

    choice = int(input("\n\tEnter choice you want to perform : "))

    if choice == 1:
        a_item = input("\n\tEnter name of item you want to add in orderlist : ")
        a_item_quantity = int(input("\tEnter quantity of item : "))
        for item in menu:
            if item[0] == a_item:
                orderList.append([item[0], item[1]*a_item_quantity, a_item_quantity])
    elif choice == 2:
        r_item = input("\n\tEnter name of item you want to remove from orderlist : ")
        for item in orderList:
            if item[0] == r_item:
                orderList.remove(item)
    elif choice == 3:
        print("\n\tItem\t\t\tPrice\t\t\tQuantity")
        print("\t------------------------------------------------------")
        for item in orderList:
            print(f"\t{item[0]}\t\t\t{item[1]}\t\t\t{item[2]}")
    elif choice == 4:
        print("\n\tItem\t\t\tPrice\t\t\tQuantity")
        print("\t------------------------------------------------------")
        for item in orderList:
            print(f"\t{item[0]}\t\t\t{item[1]}\t\t\t{item[2]}")
        print("\n\n\t------------------------------------------------------")
        sum = 0
        for item in orderList:
            sum += item[1]

        print(f"\n\tTotal : {sum}")
        break
    else:
        print("\tInvalid Choice")

    option = input("\n\tWanna perform other operations? press 'y' for yes and 'n' for no : ")
else:
    print("\n\tItem\t\t\tPrice\t\t\tQuantity")
    print("\t------------------------------------------------------")
    for item in orderList:
        print(f"\t{item[0]}\t\t\t{item[1]}\t\t\t{item[2]}")
    print("\n\t------------------------------------------------------")
    sum = 0
    for item in orderList:
        sum += item[1]

    print(f"\tTotal : {sum}")