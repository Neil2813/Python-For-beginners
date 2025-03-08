cost=int(input("Enter the cost of Bike:"))
print(f"So the cost of bike is {cost}")
if(cost>100000):
    tax=cost*0.15
    total=cost+tax
    print(f"The tax to pay for bike cost Rs.{cost} is Rs.{tax}. So the total amount is Rs.{total}")
elif(cost>50000 and cost<=100000):
    tax=cost*0.1
    total=cost+tax
    print(f"The tax to pay for bike cost Rs.{cost} is Rs.{tax}. So the total amount is Rs.{total}")
else:
    tax=cost*0.05
    total=cost+tax
    print(f"The tax to pay for bike cost Rs.{cost} is Rs.{tax}. So the total amount is Rs.{total}")