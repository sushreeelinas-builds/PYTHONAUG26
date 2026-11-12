# print("Hello From day2")

#Operators in Python

#1.Arithmetic Operators

# Operator	       Name	      
# +	           Addition	
# -	           Subtraction	
# *	           Multiplication	
# /	           Division	
# %	           Modulus	
# //	       Floor Division	
# **	       Exponentiation	


#examples
# x=5
# y=10

# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x%y)
# print(x//y)
# print(x**y)



#2.Comparison (Relational) Operators
#examples
# a = 10
# b = 5

# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)


#3.Logical Operators
#Operator	Meaning	                                     Example
#   and	    Both conditions must be True	           10 > 5 and 5 < 8
#   or	    At least one condition must be True    	   10 < 5 or 5 < 8
#   not	    Reverses the result	not                    (10 > 5)

#examples

# print(True and True and True )
# print(False or False or False)
# print(not True)

# x=5
# y=10

# print(x<10 and x==y)

#3. Membership Operators
# Membership operators check whether a value exists in a sequence such as a string, list, or tuple.

# There are two membership operators:
# - in – Returns True if the value exists.
# - not in – Returns True if the value does not exist.

# fruits = ["apple", "banana", "mango"]

# print("apple" in fruits)
# print("orange" not in fruits)

# name="Elina"


#Python Decision-Making Statements
score = 100

# if score>=30:
#     print("Pass")


# if score >=30:
#     print("Pass")
# else:
#     print("Faill")

# score=30
    
# if score ==30:
#     print("Just Pass")
# elif score > 30:
#     print("pass")
# elif score > 80:
#     print("First Class")
# else:
#     print("Fail")

# age= 55

# if age ==18:
#     print("just 18")
# if age > 18:
#     if age > 60:
#         print("Old age")
#     elif age < 60 and age > 50:
#         print("Between 50-60")
#     else:
#         print("less than 60")
# else:
#     print("less than 18")
    
    
# . Loops in Python
# A loop is used to execute a block of code repeatedly.

# Python has two main types of loops:
# 1. for loop
# 2. while loop
    
# 1. for loop
#A for loop is used to iterate over a sequence, such as a list, string, or range.
#Syntax:

# for variable in sequence:
#     # code to execute

#examples
# for i in range(5):
#     print(i)

# for i in range(5, 26, 5):
#     print(i)

# for i in range(5,0,-1):
#     print(i)

# 2.nested loop
    
# for i in range():
#     for j in range():
#         print(i, j)

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i, j)
        
    
# for i in range(5):
#     for j in range(3):
#         print(i, j)

# 3.while loop
    # while condition:
    # statement
    # increment/decrement
    
i = 5

# while i <= 5:
#     print(i)
#     i += 1
    
    
# while i >= 1:
#     print(i)
#     i -= 1


# for i in range(1, 7):
#     if i == 4:
#         print(444)
#     else:
#         print(i)
     

# for i in range(1, 5):
#     if i % 2 == 0:
#         print(i, "- Even")
#     else:
#         print(i, "- Odd")
        
#     1
#     2
#     3
#     3
#     4
#     5
    
for i in range(1,10):
    if i>=5:
        break
    print(i)
        