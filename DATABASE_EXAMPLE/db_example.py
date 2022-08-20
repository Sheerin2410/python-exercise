import pymysql
from tkinter import Button, Entry,IntVar,Label, StringVar,Tk

mydb = pymysql.connect(host="localhost",user="root",database="python_db1")


cur = mydb.cursor()

cur.execute("create table if not exists student (id int primary key AUTO_INCREMENT , name varchar(20),subject varchar(20)) ")

mydb.commit()

screen = Tk()
screen.geometry("500x500")

var_ename = StringVar()
var_subject = StringVar()
var_id = IntVar()

def inserData():
    query= "insert into student(name,subject) values ('%s', '%s') "
    values = (var_ename.get(),var_subject.get())

    cur.execute(query%values)
    print("Data Inserted |||")
    var_ename.set("")
    var_subject.set()
    mydb.commit()

def deleteData():
    query = "delete from student where id = %s "
    values = (var_id.get())
    cur.execute(query,values)
    mydb.commit()

    print("Data Deleted")


lb1_name = Label(screen,text="Enter Name : " )
lb1_name.place(x=10,y=10)

lb1_subject = Label(screen,text="Enter Subject : " )
lb1_subject.place(x=10,y=60)

ename = Entry(screen,textvariable=var_ename)
ename.place(x=150,y=10)

esubject = Entry(screen,textvariable=var_subject)
esubject.place(x=150,y=60)

btn = Button(screen,text="Submit",width=6,height=1,font=('arial',12,'bold'),command=inserData)
btn.place(x=150,y=100)

label_id = Label(screen,text="Enter Id For Delete : ")
label_id.place(x=10,y=200)

idbox = Entry(screen,textvariable=var_id)
idbox.place(x=120,y=200)

btn = Button(screen,text="Delete",width=6,height=1,font=('arial',12,'bold'),command=deleteData)
btn.place(x=180,y=195)


screen.mainloop()
