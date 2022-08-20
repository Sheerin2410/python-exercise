import tkinter

screen = tkinter.Tk()

screen.geometry("500x500")
screen.configure(bg = "pink")

#tkinter variable
var_ename_id = tkinter.StringVar()

def myfun():
    print("Welcome")
    print("Value From tkinter = ",var_ename_id.get())

#Label
lbl = tkinter.Label(screen,text="Welcome to Tkinter",font=("arial",26,"bold"),bg = "pink")
lbl.place(x=80,y=10)

#Label
l_name = tkinter.Label(screen,text="Enter Your Name : ",font=("arial",10,"bold"),bg="pink")
l_name.place(x=20,y=80)

#Entry
e1 = tkinter.Entry(screen,textvariable=var_ename_id)
e1.place(x=150,y=80)

#Button
btn = tkinter.Button(screen,text="Submit",font=("arial",10,"bold"),command=myfun)
btn.place(x=300,y=80)
screen.mainloop()