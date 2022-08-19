class employee:
    def __init__(self,first,last,pay):
        self.fname = first
        self.lname = last
        self.pay = pay
        self.email = first + '.' + last + '@eereeda.com'
    def fulname(self):
        return self.fname + ' ' + self.lname

emp_1 = employee('f1','l1',100)
emp_2 = employee('f2','l2',200)

# print(emp_2.email)
# print(emp_1.fulname())
# print(employee.fulname(emp_2))

