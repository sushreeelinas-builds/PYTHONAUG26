#1. Write a function that takes a number and checks whether it is even or odd.
# def even_odd(num):
    
#     if num % 2 == 0:
#         print("even")
#     else:
#         print("odd")
# even_odd(39)

#or using return
# def even_odd(num):
#     if num %2==0:
#         return "even"
#     else:
#         return "odd"
# print(even_odd(23))



#2. Write a function that takes a number and returns whether it is positive, negative, or zero.
# def function(num):
#     if num > 0 :
#         print("positive")
#     elif num < 0:
#         print("negative")
#     else:
#         print("Zero")
        
# function(-5)

# or using return
# def function(num):
#     if num > 0:
#         return "positive"
#     elif num <0:
#         return "negative"
#     else:
#         return "Zero"
    
# print(function(0))
    
        

#3. Write a function that takes an age and checks voting eligibility.
# def voting(age):
#     if age >=18:
#         print("Eligible to vote")
#     else:
#         print("not eligible")

# voting(10)

#or using return

# def voting(age):
#     if age >= 18:
#         return"Eligible"
#     else:
#         return"mot eligible"

# print(voting(30))
        
    
    
# Write a function that takes two numbers and returns their sum.
# def num(a,b):
#     return a+b
# print(num(10,20))


# Write a function that takes two numbers and returns the largest number.
# def numbers(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# res = numbers(50, 20)
# print(res)
# or 
# print(numbers(20,30))

# Write a function that takes a number and returns its square.
# def numbers(a):
#     return a**2
# print(numbers(3))


# Write a function that takes a number and returns its cube.
# def number(a):
#     return a**3
# print(number(2))


# Write a function that takes a number and checks whether it is divisible by 5.
# def number(a):
#     if a % 5 ==0:
#         print(a, "is divisible by 5")
#     else:
#         print(a,"is not divisible by 5")
        
# number(15)

#or using return 
# def number(a):
#     if a % 5 ==0:
#         return f"{a} is divisible by 5"
#     else:
#         return f"{a} is not divisible by 5"
        
# print(number(40))



# Write a function that takes a number and returns its multiplication table.
# def number(a):
#     for i in range(1,11):
#         print(a,"X",i,"=",a*i)
# number(3)

#using return
# def number(a):
#     result=[]
#     for i in range(1,11):
#         result.append( f"{a} X {i} = {a*i}")
#     return result
    
# print(number(4))


# Write a function that takes a name and prints a welcome message.
# def function(name):
#     print(name,"Welcome")
# function("Elina")