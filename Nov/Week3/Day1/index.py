# list
# fruits=['apple','orange','mango','banana','graphs']
# for i, fruit in enumerate (fruits):
#     print(i+1,"->",fruit)

#Tuples
# fruits=('apple','orange','mango','banana','graphs')
# for i, fruit in enumerate (fruits):
#      print(i+1,"->",fruit)
     
#sets 
# fruits={'apple','orange','mango','banana','graphs'}
# for i, fruit in enumerate (fruits):
#      print(i+1,"->",fruit)

#dict
# student = {
#     "name":"Elina",
#     "age":23,
#     "city":"bbsr"
# }
# for key in student:
#     print(key)
    
# for key,val in student.items():
#     print(key,'is',val)



#Function
#simple function
# def welcome():
#     print("Welcome to python")
# welcome()

#position Argument
# def welcome_with_name(name,age,city):
#     print("welcome",name)
#     print("age",age)
#     print("city",city)
# welcome_with_name("Rahul",23,"bbsr")  

#Keyword Argument
# welcome_with_name(age=23,name="Rahul",city="bbsr")

#Default Argument
# def welcome_with_name(name="Default",age=0,city="Default city"):
#     print("welcome",name)
#     print("age",age)
#     print("city",city)
# welcome_with_name()


#Variable Length Argument
# def showArgs(*numbers):
#     for i in numbers:
#         print(i)
        
# numbers = (10,20,30,40)

#return

# def welcome():
#     return"Welcome to python"


# res=welcome()
# print(res)


# write a fun with a args, that return the particular no is even or odd.
# def function(number):
#         if number % 2 == 0:
#             return number, "the number is even"
#         else:
#             return("odd")
# res=function(52)
# print(res)

# write a function that takes a list og numbers and return the largest number
# numbers = [10,20,500,300,1111]

# Write a function that takes a list of numbers
# and returns the largest number.

# def function(numbers):
#     largest = numbers[0]

#     for i in numbers:
#         if i > largest:
#             largest = i

#     return largest, "is the largest number"

# numbers = [10,20,500,300,1111]

# print(function(numbers))

#write  a function that takes a list of numbers and return largest and smallest numbers.
# numbers = [10,20,500,300,111,30,10]


# Write a function that takes a list of numbers
# and returns the largest and smallest numbers.

# def function(numbers):
#     largest = numbers[0]
#     smallest = numbers[0]

#     for i in numbers:
#         if i > largest:
#             largest = i

#         if i < smallest:
#             smallest = i

#     return f"largest-{largest}, smallest-{smallest}"

# numbers = [10, 20, 500, 300, 111, 30, 10]

# res = function(numbers)
# print(res)

#write a function that take a argument as age and  returns a Voting alegibility.
# -not eligible
# -eligible
# -just 18

# def voting(age):
#     if age < 18:
#         return " Not Eligible"
#     elif age >= 18:
#         return "Eligible"
#     else:
#         return "just 18 "

# res = voting(68)
# print(res)

#write a function that takes mark and show grade.
# mark-90-100 grabe-A
# mark-80-89 grade-B
# matk-70-79 grade-C
# mark-50-59 grade-D
# less then 50 fail
            
# def grade(mark):
#     if mark >= 90:
#         print("Grade A")
#     elif mark >= 80:
#         print("Grade B")
#     elif mark >= 70:
#         print("Grade C")
#     elif mark >= 60:
#         print("Grade D")
#     elif mark < 50:
#         print("Grade E")
#     else:
#         print("Fail")

# grade(75)


# write a function that takes a number list and show the numbers are even or odd
# number=[10,11,530,320,111,30,10]
# 10-"even"....

# def function(number):
#     for i in number:
#         if i % 2 == 0:
#             print(i, "- Even")
#         else:
#             print(i, "- Odd")

# number = [10, 11, 530, 320, 111, 30, 10]

# function(number)


# write a function that takes a number list and show how many even and odd are there .
# number = [10, 11, 530, 320, 111, 30, 10]

# odd numbers are 2 and even numbers are 5

# def function(number):
#     even = 0
#     odd = 0

#     for i in number:
#         if i % 2 == 0:
#             even += 1
#         else:
#             odd += 1

#     print("Odd numbers are ", odd ,"and even numbers are ",even)
    


# number = [10, 11, 530, 320, 111, 30, 10]

# function(number)


## write a function that show the mulyiplication table .

n=5

# def function(n):
#     for i in range(1, 11):
#         print(n, "x", i, "=", n * i)


# n = 5
# function(n)







