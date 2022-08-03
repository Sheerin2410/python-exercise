
import faculty,student

f = faculty.facultyclass()
s = student.studentclass()

status = True
while status:
    fname = input("Enter name of faculty : ")
    subject = input("Enter subject of faculty : ")
    contact = input("Enter contact no. of faculty : ")
    city = input("Enter city of faculty : ")
    email = input("Enter email of faculty : ")

    f.createFaculty(fname,subject,contact,city,email)

    choice = input("do you want to mare press 'y' for yes and 'n' for no :")
    if choice=='y':
        status=True
    else :
        status=False

fname = input("Enter name of student: ")
subject = input("Enter subject of student : ")
contact = input("Enter contact no. of student: ")
city = input("Enter city of student: ")
email = input("Enter email of student: ")
score = input("Enter Marks of student: ")
fees = input("Enter feesof student: ")

s.createFaculty(fname,subject,contact,city,email,score,fees)

choice = input("do you want to mare press 'y' for yes and 'n' for no : ")
if choice=='y':
    status=True
else :
    status=False
