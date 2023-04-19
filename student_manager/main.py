import student_man
while True:
    print("Welcome to the application !!")
    print("1.Registration\n","2.View student\n","3.Student update\n","4.Student delete ")
    choice=input("Enter the choice[1,2,3,4] : ")
    if choice=="1":
        print("you have chosen thr registration method !!")
        print("Welcome to register the form..")
        student_man.reg()
        print("student register succesfully !!!")
    elif choice=="2":
        print("You have chosen the view student !!")
        print("View Student")
        student_man.student_view()
    elif choice=="3":
        print("you have choosen student updated!! ")
        print("Student update")
        student_man.update_student()
    elif choice=="4":
        print("You have choosen student delete!!")
        print("Student Delete")
        student_man.student_delete()
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
    
            