import json
f=open("file.json","r")

data=json.load(f)

print(data["patient_details"][2])
f.close()

# emp_dict={
#     "patient_name":input("Enter the patient_name : "),
#     "patient_age":input("Enter the patient age : "),
#     "patient_add":input("Enter the patient add : ")
# }
# data["patient_details"].append(emp_dict)
# print(data)

# f.close()

# fw=open("file.json","w")
# json.dump(data,fw,indent=3)
# f.close()
       