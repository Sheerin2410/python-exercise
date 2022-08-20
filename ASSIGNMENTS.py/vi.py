class Idea:
    def idea(self):
        print("WELCOME TO IDEA")

class Vodafone:
    def vodafone(self):
        print("WELCOME TO VODAFONE")

class VI(Idea,Vodafone):
    def display(self):
       self.idea()
       self.vodafone()

vi =VI()
vi.display()

        
