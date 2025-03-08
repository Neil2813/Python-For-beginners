age=int(input("Enter your age?"))
if(age>=18):
    if(age>=80): #this is called nesting if statement inside a if statement
        print("You cannot drive")
    else:
        print("You can drive")
else:
    print("You cannot drive")