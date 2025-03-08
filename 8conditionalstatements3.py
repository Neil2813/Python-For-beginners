marks=float(input("Enter the marks:"))
print(f"The marks are {marks}")
if(marks>100):
    print("Marks doesnt exist")
elif(marks>=90):
    print("A+")
elif(marks<90 and marks>=80):
    print("A")
elif(marks<80 and marks>=70):
    print("B+")
elif(marks<70 and marks>=65):
    print("B")
elif(marks<65 and marks>=50):
    print("C")
else:
    print("Fail")

