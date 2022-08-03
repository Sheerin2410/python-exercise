class MobileStore:
    def __init__(self):
        self.mobile = 5000
        self.__laptop = 50000
        
    def display(self):
        print("mobile = ",self.mobile)
        print("laptop = ",self.__laptop)

    def changePrice(self,newprice):
        self.__laptop = newprice

obj = MobileStore()
obj.display()

obj.mobile = 8000
obj.__laptop = 80000
obj.display()
print("__CHANGE__PRICE")
obj.changePrice(75000)

obj.display()