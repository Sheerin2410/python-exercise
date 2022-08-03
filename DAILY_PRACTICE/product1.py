class ProductClass:
    """
    __init__ works as a constructor
     
     it automatically call when object of class create

    """
    def __init__(self):
        print("Welcome to Product Panel")
        self.mobile = 5000
        self.__laptop = 70000

    def display(self):
        print(self.mobile)
        print(self.__laptop)

    def updateprice(self,newlaptopprice):
        self.__laptop = newlaptopprice