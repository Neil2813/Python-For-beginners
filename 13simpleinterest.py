p= float(input("Enter Principle Amount:"))
r= float(input("What is the rate of interest?"))
t= float(input("The time of loan(in month):"))
name= input("Your name:")
SI=(p*t*r)/100
total= SI+p
print(f"Hello {name}. Welcome to Union Bank of India. You have applied for loan of principle amount of Rs.{p} and the rate of interest is {r}% for {t}months. So your Simple interest is calculated upto Rs.{SI}. The total amount at the time of repaying is Rs.{total}.")
print(f"Thank you {name}.")