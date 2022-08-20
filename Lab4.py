name = input("Please enter your first name : ")
if name=="":
    print("You did not enter any charecter")
elif len(name.title())==1:
     print("There is",len(name),"letters in",name.title())
elif name.isalpha():
    for index,letter in enumerate(name.title(),1):
        print(index," ",letter)
    print("There are",len(name),"letters in",name)
elif name.isalnum():
    print("Non Alphabatic charecter were entered")

else:
    f=filter(str.isalpha,name)
    str="".join(f)
    print(str)
    for index,letter in enumerate(name.title(),1):
        print(index,":",letter)
    print("There are ",len(str),"letters in" ,name.title())



