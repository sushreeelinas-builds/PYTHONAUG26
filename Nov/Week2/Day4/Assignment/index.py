# List

# 1. Create a list of 10 numbers and print all elements using a for loop.
# list=[10,20,30,40,50,60,70,80,90,100]

# for i in list:
#     print(i)


# 2. Write a program to print only even and odd numbers from a list.
# list=[1,2,3,4,5,6,7,8,9,10,12,23,45]
# even=[]
# odd=[]

# for i in list:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("even number : ",even)
# print("odd number : ",odd)


# 3. Find the largest and smallest numbers in a list using a loop.
# n=[2,4,6,5,7,8,9,3]
# largest=n[0]
# smallest=n[0]
# for i in n:
#     if i>largest:
#         largest = i
#     if i<smallest:
#         smallest = i

# print("largest no is :",largest)
# print("smallest no is :",smallest)
    
    
    

# 4. Count how many times a particular number appears in a list.
# n=[10,20,30,40,50,60,10,20,10]
# number=10
# count=0

# for i in n:
#     if i == number:
#         count=count+1
        
# print(number,"is appears",count,"times")


# 5. Write a function to calculate the sum of all elements in a list without using sum().
# n=[2,3,4,5,6,7,8,9]
# sum=0

# for i in n:
#     sum=sum+i
    
# print(sum)
    

# 6. Find the second-largest number in a list without using sort() or max().
# n=[20,30,40,50,60,70,80,90]

# largest=n[0]
# second_largest=n[0]

# for i in n:
#     if i>largest:
#         second_largest=largest
#         largest=i
        
#     elif i>second_largest and i!=largest :
        
#         second_largest=i
        
# print("largest no. is :",largest)
# print("second_largest no. is :",second_largest) 
    
        

# 7. Remove duplicate elements from a list without using set().
# n=[20,30,40,20,40,50,20,60,70]
# list=[]
 
# for i in n:
#     if i  not in list:
#         list.append(i)
        
# print(list)
        

# 8. Separate positive, negative and zero values into three different lists.
# n=[10,-5,0,6,30,-15,20,33,-75]
# positive=[]
# negative=[]
# zero=[]

# for i in n:
#     if i>0:
#         positive.append(i)
#     elif i<0:
#         negative.append(i)
#     else:
#         zero.append(i)
        
# print("Positive :", positive)
# print("Negative :",negative)
# print("Zero :", zero)

# 9. Find the common elements between two lists without using intersection().
# a=[10,20,30,40,50,60]
# b=[50,60,70,80,90,100]

# common=[]

# for i in a:
#     if i in b:
#         common.append(i)
        
# print("Common element :",common)


# 10. Write a function to check whether a list is a palindrome.

