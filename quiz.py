quiz = {
    1 : {
        "que" : "Who is the prime minister of india ?" ,
        "ans" : "modi"
    },
    2 : {
        "que" : "Most popular programming language ?" ,
        "ans" : "python"
    },
    
}
for i in range(1,len(quiz.keys())+1):
    print("Question : ",quiz[i]["que"])
    ans=input("Enter Answer :")
    if ans==quiz[i]["ans"]:
        print("Right Answer")
    else:
        print("Wrong Answer")

