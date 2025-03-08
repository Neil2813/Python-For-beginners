age=int(input("Enter your age:"))
print(f"Your age is {age}")
required=18-age
if(age>=18):
    print(f"Your {age}. So you are eligible to vote")
else:
    print(f"Your {age}. Come back after {required} years to vote")