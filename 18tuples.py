#tuple is a built in datatype that lets us create immutable sequence of values
tup=(1, 3, 4, 7)
print(type(tup))
print(len(tup))
print(tup)
print(tup[3])
tupl=() #this is also valid tuple
print(tupl)
print(type(tupl))
#if u put only 1 element in tuple its datatype will be that if 1 then int if 1.0 then float if n then string

#methods in tuple
print(tup.index(4)) #will search the index where 4 is there
print(tup.count(7)) #will count how many time the given element is there
