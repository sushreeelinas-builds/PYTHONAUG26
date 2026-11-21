# 1. Create a function to check whether a number is even or odd.
# def evenOdd(number):
#         if number % 2 == 0:
#             return number, "the number is even"
#         else:
#             return("odd")
# res=evenOdd(52)
# print(res)


# 2. Create a function to find the largest of three numbers.
# def element(a,b,c):
#     if a > b and a > c :
#         return a ,"is largest "
#     elif b > a and b > c:
#         return b , "is largest"
#     else:
#         return c,"is largest"
    
# print(element(23,45,90))
    


# 3. Create a function to calculate factorial.
# def factorial(a):
#     fact = 1
    
#     for i in range(a,0,-1):
#         fact *= i
#     return fact

# print(factorial(4)) 



# 4. Create a function to check whether a number is prime.
# def number(a):
#     for i in range(2,a):
#         if a % 2 == 0 and a >=1:
#             return "Prime"
#         else :
#             return "Not Prime"
    
        
# print(number(33))
        


# 5. Create a function to reverse a string.
# def reverse(name):
#     rev =""
    
#     for i in name:
#         rev = i+rev
#     return rev

# print(reverse("Sushree"))        
    


# 6. Create a function to calculate the sum of all elements in a list.
# a=[2,3,4,5,6,7,8]

# def function():
#     sum=0
#     for i in a:
#         sum += i
#     return sum
# print(function())



# 7. Create a calculator using separate functions for addition, subtraction, multiplication, and division.
# def calculator(a,b,operator):
#     if operator == "+":
#         return a+b
#     elif operator == "-":
#         return a-b
#     elif operator == "*":
#         return a*b
#     elif operator == "/" and b!=0:
#         return a/b
#     else:
#         return "invalid"
    
# print(calculator(20,30,"+"))
# print(calculator(45,20,"-"))
# print(calculator(20,3,"*"))
# print(calculator(40,10,"/"))
    


# 8. Create a function using `args` to calculate the sum of multiple numbers.
# def addition(*a):
#     total = 0

#     for i in a:
#         total += i
#     return total

# print(addition(10, 20, 30))
# print(addition(5, 10, 15, 20))
# print(addition(1, 2, 3, 4, 5))


# 9. Create a function using `*kwargs` to display student details.
# def student(**kwargs):
#     for key, value in kwargs.items():
#         print(key, ":", value)

# student(name="Rahul", age=22, course="MCA", marks=85)


# 10. Create a recursive function to calculate the Fibonacci sequence.

