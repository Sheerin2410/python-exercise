from abc import ABC ,abstractmethod
# ABC : Abstract Base Class
class RBI(ABC):
    @abstractmethod
    def roi(self):
        #method declaration only
        pass

class SBI(RBI):
    def roi(self):
        print("7.8")


class HDFC(RBI):
    def roi (self):
        print("6.6") 

sbi = SBI()
hdfc = HDFC()

sbi.roi()
hdfc.roi()