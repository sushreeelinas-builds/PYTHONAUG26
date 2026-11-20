# Set

#1. Create a set of 10 numbers and print all elements using a for loop.
# a={1,2,3,4,5,6,7,8,9,10}
# for i in a:
#     print(i)

#2. Create two sets and find their union.
# a={1,2,3,4,5}
# b={5,6,7,8,9,10}

# u_set=a.union(b)
# print(u_set)


#3. Find the common elements between two sets using intersection().
# a={1,2,3,4,5}
# b={5,6,7,8,9,10}

# u_set=a.intersection(b)
# print(u_set)

#4. Find the difference between two sets using difference().
# a={2,3,4,5,6}
# b={3,4,5,6,7,8,9}

# u_set=a.difference(b)
# print(u_set)


#5. Find the largest and smallest numbers in a set using a loop.
# a={10,20,30,40,50,60,222,444,500}
# largest=0
# smallest=0

# for i in a:
#     if i>largest:
#         largest=i
#     if i<smallest:
#         smallest=i
# print("Largest no :",largest)
# print("Smallest no :",smallest)


#6. Find common elements between two sets without using intersection().
# a = {10, 20, 30, 40, 50}
# b = {30, 40, 50, 60, 70}
# common = []

# for i in a:
#     if i in b:
#         if i not in common:
#             common.append(i)
# print("Common elements:", tuple(common))


#7. Find the union of two sets without using union().
# a = {10, 20, 30, 40, 50}
# b = {30, 40, 50, 60, 70}
# union = set()

# for i in a:
#     union.add(i)

# for i in b:
#     union.add(i)

# print("union :", union)


#8. Check whether two sets are equal without using the == operator.



#9. Find the elements that are present in exactly one of three sets.
# a = {10, 20, 30, 40}
# b = {30, 40, 50, 60}
# c = {40, 60, 70, 80}
# result = set()

# for i in a:
#     if i not in b and i not in c:
#         result.add(i)

# for i in b:
#     if i not in a and i not in c:
#         result.add(i)

# for i in c:
#     if i not in a and i not in b:
#         result.add(i)

# print("Elements present in exactly one set:", result)



#10. Find the common characters between two strings using sets.
# a = "Elina"
# b = "Sahoo"
# common = set()

# for i in a:
#     if i in b:
#         common.add(i)

# print("Common characters:", common)