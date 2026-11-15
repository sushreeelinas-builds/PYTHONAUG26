# 1. List – Practice Questions

# 1. Create a list of 5 numbers and print all elements.
# list=[1,2,3,4,5]
# print(list)

# 2. Find the sum of all elements in a list.
# a=[2,3,4,5,6]
# total=sum(a)
# print("Sum=",total)

# 3. Find the largest and smallest number in a list.
# a=[4,5,6,7,8]
# largest=max(a)
# smallest=min(a)

# print("largest=",largest)
# print("smallest=",smallest)

# 4. Count the total number of elements in a list.
# x=[3,4,5,6,7]
# Count=len(x)
# print("Total no. =",Count)

# 5. Reverse a list without using the reverse() method.
# x=[2,3,4,5,6,7,8]
# x.reverse()
# print(x)

# 6. Find the second-largest number in a list.
# x=[2,3,4,5,6,7]
# x=list(set(x))
# x.sort()
# print("Second-largest no. =",x[-2])

# 7. Remove duplicate elements from a list.
# x=[2,3,4,4,5,2,3]
# x=list(set(x))
# print(x)

# 8. Separate even and odd numbers from a list.
# a=[2,3,4,5,6,7,8,9,]
# even=[]
# odd=[]

# for i in a:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
    
# print("Even =",even)
# print("Odd =",odd)

# 9. Find how many times a particular element appears in a list.
# a=[10,20,30,50,20,40,50,20,90,30,60]
# count=a.count(20)
# print("20 appears =",count,"times")


# 10. Sort a list in ascending and descending order.
numbers = [50, 10, 40, 20, 30]

ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

print("Ascending:", ascending)
print("Descending:", descending)
