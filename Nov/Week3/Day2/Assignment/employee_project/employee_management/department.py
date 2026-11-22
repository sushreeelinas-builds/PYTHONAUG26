def find_by_department(employees, department):

    for emp in employees:
        if emp.department.lower() == department.lower():
            emp.display()


def highest_paid_employee(employees):

    highest = max(employees, key=lambda emp: emp.salary)

    print("Highest Paid Employee:")
    highest.display()