#Set is collection of unordered items
#set is mutable
#Each Element in The set must be unique and immutable

set_1 ={1,2,2,2}
set_2 = { "Neil", 2, 44}
print(len(set_1))
print(type(set_1))
print(set_1)
print(set_1)

#to create an empty set  name = set()
Hey = set()

#list and dictionary cant be in set because they are mutable

#methods in Set
set_1.add(3)  #add one element to set
set_1.remove(1) #remove the element from set
set_1.add(4)
set_1.add(5)
set_1.add(6)
set_1.pop()  #will remove one random element from set
print(set_1)
set_1.clear()  #will clear the set
print(set_1)
set_1.add(4)
set_1.add(5)
set_1.add(6)
print(set_1.union(set_2))  #combines both sets
print(set_1.intersection(set_2)) #combines common value from both the set

