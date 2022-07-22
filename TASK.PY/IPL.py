data = """

    -------------------------------------------------
                          ROLE
    -------------------------------------------------                      
              1:-COUNSELOR
              2:-FACULTY
              3:-STUDENT
    -------------------------------------------------
            COUNSELOR
    -------------------------------------------------          
    CHOICE 1) ADD STUDENT
    CHOICE 2) REMOVE STUDENT
    CHOICE 3) VIEW ALL STUDENT
    CHOICE 4) VIEW SPECIFIC STUDENT
    CHOICE 5) CAN ASSIGN FACULTY TO SPECIFIC STUDENT
    ------------------------------------------------
            FACULTY
    ------------------------------------------------
    CHOICE 1) ADD MARKS TO THE STUDENT
    CHOICE 2) VIEW ALL STUDENTS
    ------------------------------------------------
            STUDENT
    ------------------------------------------------
    CHOICE 1) VIEW OWN DETAILS
    CHOICE 2) PAY FEES
    
    
"""
counselor_list={}
faculty_list={}
sudent_list={}
print(data)

choice=input("enter the role you want to choose:")
if choice==1:
      print("COUNSELOR")
      add_student ={
        "sr_no":"",
        "firstname":"",
        "lastname":"",
        "contact":"",
        "faculty":"",
        "fees":""}
L1=list(add_student)
    
add_student.append('sr_no')
add_student.append('firstname')
add_student.append('lastname')
add_student.append('contact')
add_student.append('faculty')
add_student.append('fees')
add_student=dict(L1)
print(add_student)


 
