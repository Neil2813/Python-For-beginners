marks = [90, 84, 97, 92, 98, 91] #this is called list (arrays in C) 
print(marks) #string and list is similar but string is immutable(which cannot change) but list is mutable(changebale)
print(type(marks)) #datatype
print(marks[1]) #marks on index 1 will appear
print(len(marks)) #length of list
student= ["Neil", 9.24, "Cloud Computing", "Mangalore", 9008631171] #but it can be any datatype in 1 list need not be same like arrays
print(student)

#mutation of list example
student[0]= "Neil Emmanuel"
print(student)

#slicing of list:  list_name=[starting_index: ending_index] but ending index wont be included
print(student[1:4])
#slicing in list is same as slicing in string

#methods in list
list1 = [2,1,3,1]
print(list1)
list1.append(4) #adds one element at the end here 4
print(list1)
list1.sort() #sorts in ascending order
print(list1)
list1.sort(reverse=True) #sorts in descending order
print(list1)
list1.reverse() #reverses the list
print(list1)
list1.insert(1, 5) #(index, insert)
print(list1)
list1.remove(1) #removes the element once (if its there twice the first one will be deleted)
print(list1)
list1.pop(2) #removes element from the given index
print(list1)