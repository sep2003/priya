import json
import tabulate

def reg():
    name=input("Enter your name : ")
    age=input("Enter your age : ")
    duration=input("Enter your duration : ")
    temp_dic={
        "name":name,
        "age":age,
        "duration":duration
    }
    f=open("reg.json","r")
    data=json.load(f)
    f.close()
    data["student_data"].append(temp_dic)
    fw=open("reg.json","w")
    json.dump(data,fw,indent=4)
    fw.close()
    
def student_view():
    heading=["S.no","Name", "Age", "Duration"]
    f=open("reg.json","r")
    data=json.load(f)
    f.close()
    table=[]
    s_no=1
    
    
    for student_data in data["student_data"]:
        temp_list=[s_no,student_data['name'],student_data['age'],student_data['duration']]
        table.append(temp_list)
        s_no+=1
    print(tabulate.tabulate(table,headers=heading))
    
    #  print(f"{student_data['name']}\t{student_data['age']}\t{student_data['duration']}")
def update_student():
    student_view()
    f=open("reg.json","r")
    data=json.load(f)
    f.close()
    stu_choice=input("Enter the s.no of the student you want to update :" )
    print("you can update \n1.Name \n2.Age \n 3. Duration\n 4. All")
    update_choice=input("please enter your choice : ")
    sno=1
    for student in data["student_data"]:
        if str(sno)==stu_choice:
            if update_choice=="1":
                name=input("Enter update name : ")
                student["name"]=name
                print("Student data updated sucessfully!!")
            elif update_choice=="2":
                age=input("Enter updated age : ")
                student["age"]=age
                print("Student data updated sucessfully!! ")
            elif update_choice==3:
                duration=input("Enter updated duration: ")   
                student["duration"]=duration
                print("Student data updated sucessfully!!")
            elif update_choice=="4":
                student["name"]=input("Enter updated name : ")
                student["age"]=input("Enter updated age :")
                student["duration"]=input("Enter updated duration: ")
                print("Student data updated sucessfully")  
            else:
                print("Invalid choice !!")
                break
        sno+=1 
    f=open("reg.json","w") 
    json.dump(data,f,indent=3)
    f.close()  
    
def student_delete():
    student_view()
    f=open("reg.json","r")
    data=json.load(f)
    f.close()
    stu_choice=input("Enter the s.no of the student you want to delete:" )
    sno=1
    for student in data["student_data"]:
        if str(sno)==stu_choice:
            data["student_data"].remove(student)
            print("student data deleted sucessfully !!")
        sno+=1
    f=open("reg.json","w")
    json.dump(data,f,indent=3)
    f.close()
            
    
    
    