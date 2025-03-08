first=int(input("Enter the number 1:"))
second=int(input("Enter the number 2:"))
third=int(input("Enter the number 3:"))
print(f"Your 3 numbers are {first}, {second} and {third}")
if(first>second and first>third):
    print(f"{first} is the greater number")
elif(first<second and second>third):
    print(f"{second} is the greater number")
elif(third>first and third>second):
    print(f"{third} is the greater number")
else:
    print("All three are equal")