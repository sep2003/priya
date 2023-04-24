class Student:
    def __init__(self,Name,Reg_no,Age,Mark):
        self.name=Name
        self.reg_no=Reg_no
        self.age=Age
        self.mark=Mark
    def is_honour(self):
        if self.mark>=60:
            print(f"{self.name}is a honour student ")
        else :
            print(f"{self.name}is not a honour student ")
