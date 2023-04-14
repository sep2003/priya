import json
def reg():
    name=input("Enter the student name: ")
    age=input("Enter the studeent age :")
    course=input("Enter the student course : ")
    duration=input("Enter the student duration :")
    tem_dic={
        "name":name,
        "age":age,
        "course":course,
        "duration":duration
    }
    
    f=open("pri.json","r")
    data=json.load(f)
    data["student_details"].append(tem_dic)
    f.close()
    f=open("pri.json","w")
    json.dump(data,f,indent=4)
    f.close()