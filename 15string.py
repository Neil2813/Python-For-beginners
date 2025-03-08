str1="This is a string."
str2="My name is Neil Emmanuel Mathias"
len1 =len(str1) #length of string 1
len2= len(str2) #length of string 2
print(str1 + " " + str2) #concadination or addition of two strings
print(f"{len1}, {len2}")
str3="This is a string. \nMy name is Neil Emmanuel Mathias" #\n for next line
len3= len(str3) #length of string 3
print(str3)
print(len3)
str4="This is a string. \tMy name is Neil Emmanuel Mathias" #\t for extra space
len4= len(str4) #length of string 4
print(str4)
print(len4)

#slicing
#str[starting_index : ending_index] ending index wont be included
str5= "Neil Emmanuel Mathias"
print(str5[3:9])
print(str5[5:len(str5)]) #or print(str5[5:])
print(str5[:6]) #or print(str5[0:6])

#negativeslicing
str6="apple is" #A is -5 p is -4 p is -3 l is -2 and e is -1
print(str6[-3:-1]) 
print(str6.capitalize())
print(str6.endswith("le"))
print(str6.count("p"))
print(str6.replace("apple", "orange"))
print(str6.find("is"))
             
 
''' 
String Functions
str.endswith("er.") returns true if the string ends with er.
str.capitalize() capitalizes the first character
str.replace(old, new) #replaces word old with new
str.find(word) returns first index of first occurence
str.count("am) counts occurence of substring in string
'''