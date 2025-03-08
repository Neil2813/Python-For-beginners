units=float(input("Enter number of units recorded:"))
if(units<=100):
    cost=0*units
    print(f"Your electricity bill is {cost}")
elif(units>100 and units<=200):
    cost=5*(units-100)
    print(f"Your electricity bill is {cost}")
else:
    cost=(10*(units-200))+500
    print(f"Your electricity bill is {cost}")
    