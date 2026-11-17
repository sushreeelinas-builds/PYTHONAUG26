# file = open("Student.txt","x")
# file.close()
# print("Student file created")

# file = open("Student.txt","r")
# print("file open")
# file.close()


# file = open("Student.txt","r")
# info=file.read()
# print(info)
# file.close


#read 1st line
# file = open("Student.txt","r")
# info=file.readline()
# print(info)
# file.close()


#read each line
# file = open("Student.txt","r")
# info=file.readlines()
# print(info)
# file.close()

#add text in same line
# file = open("Student.txt","w")
# file.write("This is new line student-4\n")
# file.write("This is new line student-5\n")
# file.write("This is new line student-6\n")
# file.write("This is new line student-4\n")
# file.close()
# print("New text added in student file")


# #add text in each line
# file = open("Student.txt","w")
# file.write("This is new line student-4")
# file.write("This is new line student-5")
# file.write("This is new line student-6")
# file.write("This is new line student-4")
# file.close()
# print("New text added in student file")

#list add in file with new lines
# students=["student-1\n","student-2\n","student-3\n","student-4\n"]
# file = open("Student.txt","a")
# file.writelines(students)
# file.close()
# print("New text added in student file")

# students=["student-1\n","student-2\n","student-3\n","student-4\n"]
# file = open("Student.txt","w")
# file.writelines(students)
# file.close()
# print("New text added in student file")

# import os
# os.rename("Student.txt", "Student-renamed.txt")
# print("renamed succefully")

# import os
# os.remove( "Student-renamed.txt")
# print("delete succefully")

# import os
# file=os.path.exists("student.txt")
# if file:
#     print("file exists")
# else:
#     print("file does't exists")


# import os
# size=os.path.getsize("student.txt")
# print(size)

# import os
# os.makedirs("student")
# print("dictionary created")

import csv
with open("students.csv","w",newline="")as file:
    wr = csv.writer(file)
    
    wr.writerow(["Name","age","address"])
    wr.writerow(["str1","20","bbsr"])
    wr.writerow(["str2","22","ctc"])
    wr.writerow(["str3","23","bbsr"])
    
print("csv file created")


# import json
# student={
#     "name":"std-1",
#     "age":23,
#     "city":"bbsr"
# }
# with open("student.json","w") as file:
#     json.dump(student,file,indent=4)
    
    
    
# import json
# with open("student.json","r") as file:
#     data=json.load(file)
# print(data['name'])
