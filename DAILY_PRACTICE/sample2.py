import tkinter
import random

screen=tkinter.Tk()
screen.title("ROCK PAPER SCISSOR")
screen.geometry("500x500")

var_user_choice = tkinter.StringVar()
var_com_choice = tkinter.StringVar()
var_result_choice = tkinter.StringVar()
com_score = 0


game_list =["ROCK","PAPER","SCISSOR"]

def myfun(msg):
    
    com_score = 0
    user_score = 0


    var_user_choice.set(msg)
    com = random.choice(game_list)
    var_com_choice.set(com)
    

    if msg==com:
        var_result_choice.set("TIE")
    
    else:
        if msg=="ROCK" and com=="PAPER":
           var_result_choice.set("COMPUTER WON")
           com_score+=1


        elif msg=="ROCK" and com=="SCISSOR":
            var_result_choice.set("USER WON")
            user_score+=1

        elif msg=="PAPER" and com=="ROCK":
            var_result_choice.set("USER WON")
            user_score+=1

        elif msg=="PAPER" and com=="SCISSOR":
            var_result_choice.set("COMPUTER WON")
            com_score+=1

        elif msg=="SCISSOR" and com=="ROCK":
            var_result_choice.set("COMPUTER WON")
            com_score+=1

        elif msg=="SCISSOR" and com=="PAPER":
            var_result_choice.set("USER WON")
            user_score+=1

        
        


btn=tkinter.Button(screen,text="ROCK",font=('arial',20,'bold'),bg="blue",fg="white",activebackground="black",activeforeground="white",command=lambda: myfun("ROCK"))
btn.place(x=10,y=10)

btn=tkinter.Button(screen,text="PAPER",font=('arial',20,'bold'),bg="blue",fg="white",activebackground="black",activeforeground="white",command=lambda: myfun("PAPER"))
btn.place(x=150,y=10)

btn=tkinter.Button(screen,text="SCISSOR",font=('arial',20,'bold'),bg="blue",fg="white",activebackground="black",activeforeground="white",command=lambda: myfun("SCISSOR"))
btn.place(x=300,y=10)

user = tkinter.Label(screen,text="USER",font=('arial',14,'bold'))
user.place(x=10,y=150)

computer = tkinter.Label(screen,text="COMPUTER",font=('arial',14,'bold'))
computer.place(x=10,y=200)

score = tkinter.Label(screen,text="score=",font=('arial',14,'bold'))
score.place(x=240,y=150)



user = tkinter.Label(screen,textvariable=var_user_choice,font=('arial',14,'bold'))
user.place(x=150,y=150)

computer = tkinter.Label(screen,textvariable=var_com_choice,font=('arial',14,'bold'))
computer.place(x=150,y=200)

score = tkinter.Label(screen,text="score=",font=('arial',14,'bold'))
score.place(x=240,y=200)


btn=tkinter.Button(screen,textvariable=var_result_choice,font=('arial',20,'bold'),bg="blue",fg="white",activebackground="black",activeforeground="white",width="25")
btn.place(x=10,y=400)

screen.mainloop()