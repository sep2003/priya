import student
while True:
        
    print("Welcome to registration form !!")
    print("REGISTER FORM...")
    print("Welcome to basic course of computer aplication...")
    choice=input("Enter the choice : ")


    if choice=="1":
        student.reg()
        if_continue=input("Do you want to reister again y/n :")
        if if_continue=="y":
            continue
        else:
            break

print("thks for using this application !!")