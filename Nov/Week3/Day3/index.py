#oop
#class and object
#method
#constructor

# class Employee:
#     emp_id = 1
#     salary = 50000
#     name = "Rahul"
#     dept = "IT"
    
# emp1 = Employee()
# emp2 = Employee()
# emp3 = Employee()

# print(emp1.name)
# print(emp2.name)


# #Method
# class Mobile :
#     brand = "IPhone"
#     price = 100000
    
#     def Ringing(self):
#         print("incomming call",self.brand)
        

# mobile1 = Mobile()
# print(mobile1.price)



# class Employee:
#     def __init__(self):
#         print("constructor 1")
        
#     def __init__(self):
#         print("constructor 2")
        
# emp1 = Employee()
# emp2 = Employee()


# class Employee:
#     name = "Rahul"
#     salary = 50000
    
#     def __init__(self):
#         self.address = "bbsr"
#         print("constructor 1")
        
# emp1 = Employee()
        
# print(emp1.name)
# print(emp1.address)


# class Employee:
#     def __init__(self,name,salary,address):
#         self.name = name
#         self.salary = salary
#         self.address = address
        
#     def EmployeeDetails(self):
#         print("Employee Name", "Elina")
#         print("Employee Salary", 50000)
#         print("Employee Address:", "bbsr")
        
# # Creating objects
# emp1 = Employee("Elina", 30000, "Bhubaneswar")
# emp2 = Employee("Sushree", 40000, "Cuttack")

# emp1.EmployeeDetails()


#make a class where i can create multiple object (employee) salary will the Fix.
# class Employee:

#     def __init__(self, name):
#         self.name = name
#         self.salary = 4500 

#     def EmployeeDetails(self):
#         return f"Hii {self.name}, your salary is {self.salary}"


# e1 = Employee("Rahul")
# e2 = Employee("Elina")
# e3 = Employee("Sushree")
# e4 = Employee("Roji")

# print(e1.EmployeeDetails())
# print(e2.EmployeeDetails())
# print(e3.EmployeeDetails())
# print(e4.EmployeeDetails())


# make a calculator with multiple methods like add ,sub,multi,division 

# class Calculator:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def add(self):
#         return self.x + self.y

#     def sub(self):
#         return self.x - self.x

#     def multi(self):
#         return self.x * self.y

#     def div(self):
#         return self.x / self.y
       

# cal = Calculator(40, 10)

# print("Addition:", cal.add())
# print("Subtraction:", cal.sub())
# print("Multiplication:", cal.multi())
# print("Division:", cal.div())


# make a class for bank passbook from where a passholder ,user can deposite  ,user can withdraw and can view there balance.
class Bank:

    def __init__(self, name, balance=50000):
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        return f"Amount deposited: {amount}"
    def withdraw(self, amount):
        self.balance = self.balance - amount
        return f"Amount withdraw: {amount}"
    def viewbalance(self):
        return
        
    
user1 = Bank("Elina")
user2 = Bank("Rahul",  10000)

print(user1.deposit(2000))
print(user1.withdraw(1000))
