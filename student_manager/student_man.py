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
    heading=["Name", "Age", "Duration"]
    f=open("reg.json","r")
    data=json.load(f)
    f.close()
    table=[]
    
    
    for student_data in data["student_data"]:
        temp_list=[student_data['name'],student_data['age'],student_data['duration']]
        table.append(temp_list)
    print(tabulate.tabulate(table,headers=heading))
    #  print(f"{student_data['name']}\t{student_data['age']}\t{student_data['duration']}")
   
        
    
    