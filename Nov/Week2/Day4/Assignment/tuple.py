# Tuple

# 1. Create a tuple of 10 numbers and print all elements using a for loop.
# a=(10,20,30,40,50,60)

# for i in a:
#     print(i)


# 2. Print all elements along with their index using enumerate().
# a=(1,2,3,4,5,6,7,8,9)

# for i in enumerate(a):
#     print(i)


# 3. Find the largest and smallest numbers in a tuple using a loop.
# a=(1,2,3,4,5,6,7,8,9)
# largest=a[0]
# smallest=a[0]

# for i in a:
#     if i > largest:
#         largest=i
#     if i < smallest:
#         smallest=i
        
# print("Largest no is :",largest)
# print("Smallest no is :",smallest)
        

# 4. Count how many times a particular number appears using count().
# a = (10, 20, 30, 20, 40, 20, 50, 20)

# num = 20

# result = a.count(num)

# print( num, "appears", result,"times")



# 5. Calculate the sum of all tuple elements without using sum().
# a=(1,2,3,4,5,6,7,8,9)

# sum=0
# for i in a:
#     sum = sum+i
    
# print(sum)
    
    
# 6. Find the second-largest number in a tuple without using sort() or max().
# a=(10,20,30,40,50,60)

# largest=a[0]
# second_largest=a[0]

# for i in a:
#     if i>largest:
#         second_largest=largest
#         largest = i
#     if i>second_largest and i!= largest:
#         second_largest = i
        
# print("largest no :",largest)
# print("Second largest no :",second_largest)


# 7. Find all duplicate elements in a tuple.
# n=(20,30,40,20,40,50,20,60,70)
# list=[]
# duplicate=[]

# for i in n:
#     if i not in list:
#         list.append(i)
#     elif i not in duplicate:
#         duplicate.append(i)
        
# print("Duplicate element :",duplicate)


# 8. Check whether a tuple is a palindrome without using slicing.




# 9. Find the common elements between two tuples using loops.
# a = (10, 20, 30, 40, 50)
# b = (30, 40, 50, 60, 70)

# common = []

# for i in a:
#     if i in b:
#         if i not in common:
#             common.append(i)

# print("Common elements:", tuple(common))



# 10. Separate even and odd numbers from a tuple into two different lists.
# a = (10, 15, 20, 25, 30, 35, 40, 45)

# even = []
# odd = []

# for i in a:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

# print("Even numbers:", even)
# print("Odd numbers:", odd)