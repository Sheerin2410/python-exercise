import random
for i in range(80):
    print("*",end="")
    

print()
print("\t\t\t        Welcome to")
print("\t\t\tKBC QUIZE")
for i in range(80):
    print("*",end="")

print()
a=input("\tEnter Your Name - ")
for i in range(80):
    print("*",end="")
 
print()
print("\n\t\tOK ",a," Let's Start The Game")

questions=["Jimmy's father has three sons- Paul I and Paul II. Can you guess the name of the third son? ","You're 4th place right now in a race. What place will you be in when you pass the person in 3rd place?","How many months have 28 days?","There are two clocks of different colors: The green clock is broken and doesn't run at all, but the yellow clock loses one second every 24 hours. Which clock is more accurate? ","If a leaf falls to the ground in a jungle, and no one hears it, will it make a sound? "]
answer=["jimmy","3rd","all months","Green clock","yes"]
wronganswers=[["Paul II","Paul III","Paul I"],["1st","2nd","4th"],["1","2","Depends if there's a leap year or not"],["yellow clock","none","both"],["no","depend on how the heavy leaf was","depend on the palce it lands"]]

attempquestion=[]
count=0
amount=0
while True:
    while True:
        selectquestion=random.choice(questions)
        if selectquestion in attempquestion:
            pass
        elif selectquestion not in attempquestion:
            attempquestion.append(selectquestion)
            questionindex=questions.index(selectquestion)
            correctanswer=answer[questionindex]
            break
    optionslist=[]
    inoptionlist=[]
    optioncount=1
    count+=1
    while optioncount<4:
        optionselection=random.choice(wronganswers[questionindex])
        if optionselection in inoptionlist:
            pass
        elif optionselection not in inoptionlist:
            optionslist.append(optionselection)
            inoptionlist.append(optionselection)
            optioncount+=1    
    optionslist.append(correctanswer)
    alreadydisplay=[]
    optiontodisplay=[]
    a1=True
    while a1:
        a=random.choice(optionslist)
        if a in alreadydisplay:
            pass
        else:
            alreadydisplay.append(a)
            optiontodisplay.append(a)
            a1=not True
    a1=True
    while a1:
        b=random.choice(optionslist)
        if b in alreadydisplay:
            pass
        else:
            alreadydisplay.append(b)
            optiontodisplay.append(b)
            a1=not True
    a1=True
    while a1:
        c=random.choice(optionslist)
        if c in alreadydisplay:
            pass
        else:
            alreadydisplay.append(c)
            optiontodisplay.append(c)
            a1=not True
    a1=True
    while a1:
        d=random.choice(optionslist)
        if d in alreadydisplay:
            pass
        else:
            alreadydisplay.append(d)
            optiontodisplay.append(d)
            a1=not True
    right_answer=""
    if correctanswer==a:
        right_answer="a"
    elif correctanswer==b:
        right_answer="b"
    elif correctanswer==c:
        right_answer="c"
    elif correctanswer==d:
        right_answer="d"
    print("--------------------------------------------------------------------------------------------")
    print("\t\t\tAmount Win - ",amount)
    print("--------------------------------------------------------------------------------------------")

    print("\n\t\tQuestion ",count," on your Screen")
    print("--------------------------------------------------------------------------------------------")
  
    print("  |  Question - ",selectquestion)
    print("--------------------------------------------------------------------------------------------")
    print("\t-----------------------------------------------------------------------------")
    
    print("\t|  A. ",a)
    print("\t-----------------------------------------------------------------------------")

    print("\t|  B. ",b)
    print("\t-----------------------------------------------------------------------------")
   
    print("\t|  C. ",c)
    print("\t-----------------------------------------------------------------------------")
   
    print("\t|  D. ",d)
    print("\t-----------------------------------------------------------------------------")
    useranswer=input("\t\tEnter Correct Option\t   or \t press Q to quit.\n\t\t\t...").lower()
    if useranswer==right_answer:
        if count==1:
            amount+=50
            print("\n\n\t\t You Won Rs. ",amount)
            
            print()
    
        print("\t\t\t|||||||||| Right Answer ||||||||||")
        print("*********")
        
    else :
        if useranswer not in answer:
         amount-=50
        print("\n\n\t\t You Won Rs. ",amount)