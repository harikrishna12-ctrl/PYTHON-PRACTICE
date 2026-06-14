#accesing one class element to the another class element is
#called inheritence 

class student:
    start_time="10am"
    end_time="6pm"


class teacher(student):
    def __init__(self,subject):
        self.subject=subject

t1=teacher("maths")


print(t1.subject,t1.start_time)