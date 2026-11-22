import employee_management

emp1 = employee_management.Employee(101, "Elina", "IT", 30000)
emp2 = employee_management.Employee(102, "Rahul", "HR", 25000)
emp3 = employee_management.Employee(103, "Priya", "IT", 40000)

employees = [emp1, emp2, emp3]

print("Employee Details")

for emp in employees:
    emp.display()
    print()

print("Salary Details")

for emp in employees:
    print(emp.name)

    print("Annual Salary:",
          employee_management.calculate_annual_salary(emp.salary))

    print("Bonus:",
          employee_management.calculate_bonus(emp.salary))
    print()

print("IT Department Employees")

employee_management.find_by_department(employees, "IT")

print("\nHighest Paid Employee")

employee_management.highest_paid_employee(employees)