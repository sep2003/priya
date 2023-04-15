import json
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
    
    