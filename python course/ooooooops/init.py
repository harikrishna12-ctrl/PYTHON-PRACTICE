class student:
    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa
        self.subject = "ai and ml"

stud1=student("hari",8.0)   
stud2=student("reddy",9.5)        
stud1=student("hari",9.3)             


print(stud2.name,stud2.cgpa,stud2.subject)