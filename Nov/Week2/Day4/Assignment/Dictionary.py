# Dictionary

# 1. Create a dictionary containing 5 students and their marks. Print all keys and values using a loop.
# student={
#     "Rahul" : 90,
#     "Ravi" : 85,
#     "Priya" : 95,
#     "Kavita" : 60,
#     "Roji" :75
# }
# for key,val in student.items():
#      print(key,"=",val)
     

# 2. Add a new key called city to an existing dictionary.
# student={
#     "name" : "Rahul",
#     "age" :23,
# }

# student["city"] = "Bhubaneswar"
# print(student)

# 3. Update the marks of a particular student.
# student={
#     "name" : "Ravi",
#     "age" : 23,
#     "mark" : 95
# }
# student["mark"] = 85

# print(student)


# 4. Find the total marks of all students without using sum().
# student={
#     "Rahul" : 90,
#     "Ravi" : 85,
#     "Priya" : 95,
#     "Kavita" : 60,
#     "Roji" :75
# }
# sum=0
# for marks in student.values():
#     sum += marks
# print("Total mark :",sum)


# 5. Count how many students passed and failed. Consider 40 as the passing mark.
# student={
#     "Rahul" : 90,
#     "Ravi" : 85,
#     "Priya" : 55,
#     "Kavita" : 20,
#     "Roji" :75
# }
# passed = 0
# fail = 0

# for marks in student.values():
#     if marks >= 40:
#         passed = passed + 1
#     else:
#         fail = fail + 1
        
# print("total pass :",passed)
# print("total fail :",fail)
        

# 6. Find the student with the highest and lowest marks without using max() or min().
# student={
#     "Rahul" : 90,
#     "Ravi" : 85,
#     "Priya" : 55,
#     "Kavita" : 20,
#     "Roji" :75
# }
# highest = 0
# lowest = 0

# for marks in student.values():
#     if marks > highest:
#         highest = marks
#     if marks < lowest:
#         lowest = marks
        
# print("Highest mark :",highest)
# print("Lowest mark :",lowest)


# 7. Find the second-highest marks from a student dictionary.
# student={
#     "Rahul" : 90,
#     "Ravi" : 85,
#     "Priya" : 55,
#     "Kavita" : 20,
#     "Roji" :75
# }
# highest = 0
# second_highest = 0

# for marks in student.values():
#     if marks > highest:
#         second_highest = highest
#         highest = marks
#     if marks > second_highest and marks != highest:
#         second_highest = marks
        
# print("Highest mark :",highest)
# print("Second_highest :",second_highest)



# 8. Create a new dictionary containing only students who scored more than 75.
# student={
#     "Rahul" : 90,
#     "Ravi" : 85,
#     "Priya" : 55,
#     "Kavita" : 20,
#     "Roji" :75
# }
# above_student = {}
# for name,marks in student.items():
#     if marks > 75 :
#         above_student[name] = marks
        
# print("Students scored more than 75 :",above_student)


# 9. Find the frequency of each character in a string and store it in a dictionary.



# 10. Merge two dictionaries without using the update() method.
student_1 = {
    "Rahul": 90,
    "Ravi": 85
}
student_2 = {
    "Priya": 95,
    "Kavita": 80
}
student_3 = {}

for name, marks in student_1.items():
    student_3[name] = marks

for name, marks in student_2.items():
    student_3[name] = marks
    
print("Merged Dictionary:", student_3)