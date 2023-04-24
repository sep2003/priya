from mcq import Mcq
print("Welcome to general knowledge question !!")

que=["1.Which is the coldest location in the earth?\na)East Antarctica b)West Antarctica 3)North Antractic",
"2.Which is the highest peak in India?\na)Mount Everst b)Mount k2 C)Mount k3",
"3.The second highest peak in  India?\na)Mount K2 b)Mount K3 c)Mount",
"4.which is the continent with the most number of countries?\na)America b)Africa c)japan"]

test=[Mcq(que[0],"a"),Mcq(que[1],"a"),Mcq(que[2],"a"),Mcq(que[3],"b")]

def run_test():
    score=0
    for ques in test:
        print(ques.Qusetion)
        answer=input("Enter your Answer: ")
        if answer==ques.Answer:
            score+=1
    print(f"Your score is {score}/{len(test)} ")
run_test()
        
        
        