import student_man
while True:
    print("Welcome to the application !!")
    print("1.Registration ","2.View student")
    choice=input("Enter the choice[1,2] : ")
    if choice=="1":
        print("you have chosen thr registration method !!")
        print("Welcome to register the form..")
        student_man.reg()
        print("student register succesfully !!!")
    elif choice=="2":
        print("You have chosen the view student !!")
        print("View Student")
        student_man.student_view()
    else:
        print("Invalid choice!!")
        
    cont=input("Do you want to continue (y/n) ? :")
    if cont=="y":
        continue
    elif cont=="n":
            break
    else:
        break
print("Thaknk you !!")
    
            