#dictionaries are used to store data values in "key":value pairs
#they are unordered, mutable and dont allow duplicate keys
#key can be boolean value, tupple, string, int, float bcz they are immutable
#key cannot be list and dictionary bcz they are mutable
info = {
    "Name" : "Neil Emmanuel Mathias",
    "Age" : 19,
    "coding" : ["C", "Python", "Java"],
    "movies" : ("Salaar", "Saaho"),
    "cgpa" : 9.24,
    "Adult" : True
}
print(info)
print(info["Name"])
info["movies"] = ("Salaar", "Saaho", "Bramayugam") #modified the dictionary key movies 
info["Single"] = False #added a new key value pair
print(info)
print(info["movies"])

# you can also create a null dictionary
dict = {}
print(dict)