#program to create an employee class

class Employee:
    def __init__(self,empid,empname,salary):
        self.empid = empid
        self.empname = empname
        self.salary = salary

    def employeeInformation(self):
        print("Employee ID:",self.empid)
        print("Employee Name:",self.empname)
        print("Employee Salary:",self.salary)

empdata = []
for i in range(5):
    id = int(input())
    name = input()
    salary = int(input())
    emp = Employee(id,name,salary)
    empdata.append(emp)
for x in empdata:
    x.employeeInformation()



