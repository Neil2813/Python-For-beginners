Personal_info = {
    "Name" : "Neil Emmanuel Mathias", 
    "Register Number" : "RA2311028010166",
    "Section" : "W1",
    "Brach" : "Networking and Communication",
    "Specialization" : "Computer Science with Cloud Computing",
    "Grade" : {
        "Operating System" : "A+",
        "Data Structures and Algorithm" : "A+",
        "Design Thinking and methodology" : "O",
        "Numerical Method and Analysis" : "O",
        "Advanced Programming and Paradigms" : "A+",
        "Computer Organization and Architecture" : "A+"
    },
    "SGPA" : 9.30
}
print(Personal_info)
print(Personal_info["Grade"])
print(Personal_info["Grade"]["Operating System"])


#methods in dictionary
"""
print(Personal_info.items())  #gives value in tuples
pairs=list(Personal_info.items())  #converts to list
print(pairs[2])  #gives the item iat index 2
"""
Personal_info.update({"City" : "Chennai"})
print(Personal_info)
"""
print(Personal_info.get("Name"))
"""

"""
#typecasting a dictionary
print(list(Personal_info.keys()))  #converted dictionary key to list
print(list(Personal_info.values()))   #converted dictionary value to list
"""
