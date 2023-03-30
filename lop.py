print("Welcome to the puzzel !!")
print("today question : i am a friut and iam red in color !!")
i=0
while i<4:
    ans=input("Enter your ans : ")
    if ans=="apple":
        print("you win !!")
        exit()
        
    elif i==0:
        print("clue 1: i am red in color.")
        
    elif i==1:
        print("clue: i am healthy friut.")
        
    elif i==2:
        print("clue 3: i am childern fav fruit.")
   
    i=i+1
        
print("you lose!!")