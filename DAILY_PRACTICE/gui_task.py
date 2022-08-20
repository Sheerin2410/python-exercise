from itertools import count
import tkinter

screen = tkinter.Tk()

screen.geometry("500x500")
screen.configure(bg="pink")

lbl = tkinter.Label(screen,text="Welcome to Tkinter",font=("arial",26,"bold"),bg = "gray")
lbl.place(x=80,y=10)
var_num = tkinter.StringVar()
count = 0
def myfun_like():
    global count
    count+=1
    print("LIKE = ",count)

def myfun_dislike():
    global count
    count-=1
    print("DISLIKE = ",count)
    
btn1 = tkinter.Button(screen,text="LIKE",font=("arial",15,"bold"),command=myfun_like)
btn1.place(x=150,y=100)

btn2 = tkinter.Button(screen,text="DISLIKE",font=("arial",15,"bold"),command=myfun_dislike)
btn2.place(x=250,y=100)

l_name = tkinter.Label(screen,text="TOTAL LIKE = ",font=("arial",12,"bold"),bg="pink")
l_name.place(x=20,y=110)

screen.mainloop()