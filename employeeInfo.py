#program to store employee information without objects

empid = 1
empname = "Alan"
designation = "Web Developer"
company = "amazon"

def empInformation(empid,empname,designation,company):
    print("Employee ID:",empid)
    print("Employee Name:",empname)
    print("Designation:",designation)
    print("Company:",company)

print("Employee Details:")
print(empInformation(empid,empname,designation,company))