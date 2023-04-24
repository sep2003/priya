class Employee:
    def __init__(self,emp_id,emp_salary,emp_experience,emp_dob):
        self.Emp_id=emp_id
        self.Emp_salary=emp_salary
        self.Emp_experience=emp_experience
        self.Emp_dob=emp_dob
    def bon(self):
        self.final_salary=(10/100)*self.Emp_salary+self.Emp_salary
        print(self.final_salary)
    def Emp_expe(self):
        if self.Emp_experience>=5:
            print((20/100)*self.Emp_salary+self.Emp_salary)
            print(self.Emp_experience)
        else:
           print((5/100)*self.Emp_salary+self.Emp_salary)
           print(self.Emp_experience)