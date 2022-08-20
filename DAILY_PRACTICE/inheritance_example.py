data = """
                        SELECT YOUR ROLE :
                        
                        press 1 for doctor 
                        press 2 for patient 
"""
print(data)
choice =int(input("Enter your Choce here : "))
if choice==1:

    class User:
       def __init__(self):
        print("USER CLASS")

       def input(self):
        self.email = input("Enter Email : ")
        self.password = input("Enter Password : ")

    class Doctor(User):
        def doc_input(self):
           self.specification = input("Enter Specification : ")

        def display(self):
         print("Doctor Email = ",self.email)
         print("Doctor Password = ",self.password)
         print("Doctor Specification = ",self.specification)

    doctor = Doctor()
    doctor.input()
    doctor.doc_input()
    doctor.display()

elif choice==2:
    class User:
       def __init__(self):
        print("USER CLASS")
    class Patient(User):
        def patient_input(self):
            self.bloodgroup = input("Enter BloodGroup : ")

    def dp(self):
        print("Doctor Email = ",self.email)
        print("Doctor Password = ",self.password)
        print("BloodGroup Of Patient = ",self.bloodgroup)
        
        
    patient = Patient()
    patient.patient_input()
    patient.input()
    patient.dp()



        