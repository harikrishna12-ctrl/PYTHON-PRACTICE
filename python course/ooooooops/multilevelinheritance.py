class employee:
    start_time="10am"
    end_time="5pm"


class adminstaff(employee):
    def __init__(self,role):
        self.role=role


class account(adminstaff):
    def __init__(self,salary,role):
        
        super().__init__(role)
        self.salary=salary


acc1=account(23,"ca")

print(acc1.salary)