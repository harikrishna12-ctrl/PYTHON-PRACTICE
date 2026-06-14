class teacher:
    def __init__(self,salary):
      self.salary=salary


class student:
   def __init__(self,gpa):
      self.gpa=gpa


class info(teacher,student):
   def __init__(self, salary,gpa,name):
      super().__init__(salary)
      student.__init__(self,gpa)
      self.name=name


infor=info(500000,"9.3","hari")

print(infor.salary,infor.gpa,infor.name)