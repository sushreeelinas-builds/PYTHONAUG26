# Non-Primitive data typea
# main difference

                # Lists         Tuples          Sets              Dictionaties
# ordering        ordered         ordered       unordered           ordered/key format
# indexing        indexed         indexed       not indexed         keyed
# mutability      mutable         immutable     mutable             mutable
# Duplictes
# allowed         yes             yes           no                  yes
# type allowed    mutabie 
#                 and immutabie


# 1.list=[1,2,3,4]
# print(list)
# print(list[0])
# a=list.append(50)
# print(list)



#2. tuple=(1,2,3,4)
# print(tuple)
# print(tuple[2])
# a=tuple.append(50)
# print(list)

# 3.set={1,2,3,4}
# print(set)

# 4.dic={"name":"Elina","age":23}
# print(dic)



#Python Non-Primitive Data Types Methods.
#Python provides built-in methods to perform operations on List, Tuple, Set, and Dictionary.

# list

# Method	        Use
# append()	  Adds one element at the end
# extend()	  Adds multiple elements
# insert()	  Adds an element at a specific position
# remove()	  Removes a particular value
# pop()	      Removes an element by index
# clear()	  Removes all elements
# sort()	  Sorts elements
# reverse()	  Reverses the list
# index()	  Returns the index of an element
# count()	  Counts occurrences
# copy()	  Creates a shallow copy

# list=[10,20,30,40]
# list.append(50)
# list.extend([50,60,70])
# list.insert(1,60)
# list.insert(60,6)
# list.remove(20)
# list.pop()
# list.pop(2)
# list.clear()
# a=list.index(30)
# print(a)

# print(list)


# Tuple Methods
# Tuple uses (). It is immutable, so we cannot add, remove, or modify its elements.
# Tuple has only two built-in methods.

# tuple=(1,2,3,4,5,6,7,8,9,1,2,2,3,3,4,3,4,5,6,7,8,9,6,6,7)
# print(tuple.count(20))
# print(tuple.index(3))



#set
# set_A={1,2,3,4}
# set_B={4,5,6,7}
# set_A.add(5)
# set_A.update([9,6])
# set_A.remove(2)  # if any value in not in the set it will show the error
# set_A.discard(2) # if any value in not in the set it will show thw set
# u_set=set_A.union(set_B)
# u_set=set_A.intersection(set_B)
# u_set={5,4}.issubset(set_B)

# print(u_set)

# print(set_A)


#dic

dict={
    "name":"sushree",
    "age":23
}
# print(dict.get("name"))
# print(dict.get("hii"))
# print(dict.keys())
# print(dict.values())
# dict.update({"name":"Sushree","age":22})
# dict.clear()
a=dict.copy()
print(dict)
