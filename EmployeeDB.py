import pandas as pd

class employee:
    def __init__(self, name , job, salary):
        self.name = name
        self.job = job
        self.salary = salary
        
    def to_dict(self):
        return {
            "Name" : self.name,
            "Job" : self.job,
            "Salary" : self.salary
        }
        
employees = {}

def add_emp():
    emp_id = input("Enter employee's ID:")
    
    if emp_id in employees:
        print("This employee already exists.")
        
    name = input("Enter the employee's name:")
    job = input("Enter the employees's job:")
    salary = float(input("Enter the employee's salary:"))
    
    employees[emp_id] = employee(name, job, salary)
    print("Done adding employee!")

def print_employees():
    if not employees:
        print("No employees in the system.")
        return
    for emp_id, emp in employees.items():
        print(f"ID: {emp_id}, Name: {emp.name}, Job: {emp.job}, Salary: {emp.salary}")
    
def print_emp_data():
    emp_id = input("Enter the employee's ID whose data is required:")
    if emp_id in employees:
        emp = employees[emp_id]
        print(f"ID: {emp_id}, Name: {emp.name}, Job: {emp.job}, Salary: {emp.salary}")
    else:
        print("Employee isn't on the system")
    
def remove_emp():
    emp_id = input("Enter the employee's ID whom you want to remove from the system:")
    if emp_id in employees:
        del employees[emp_id]
        print("Employee deleted!")
    else:
        print("Employee isn't found")

def update_emp():
    emp_id = input("Enter Employee's ID to update:")
    if emp_id not in employees:
        print("Employee isn't found")
        return
    name = input("Enter new name: ")
    job = input("Enter new job: ")
    salary = float(input("Enter new salary: "))
    employees[emp_id] = employee(name, job, salary)
    print("Employee updated!")
    
def export_to_excel():
    data = {emp_id : emp.to_dict() for emp_id, emp in employees.items()}
    df = pd.DataFrame.from_dict(data, orient = 'index')
    df.to_excel('EmployeeDatabase.xlsx')
    print("Exported to EmployeeDatabase.xlsx")
    
while True:
    print("\nEmployee Management System\n1. Add Employee\n2. View All Employees\n3. View one employee\n4. Remove Employee\n5. Update Employee\n6. Export to Excel\n7. Exit\n")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_emp()
    elif choice == "2":
        print_employees()
    elif choice == "3":
        print_emp_data()
    elif choice == "4":
        remove_emp()
    elif choice == "5":
        update_emp()
    elif choice == "6":
        export_to_excel()
    elif choice == "7":
        break
    else:
        print("Invalid choice. Try again.")