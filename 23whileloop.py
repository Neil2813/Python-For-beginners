#loops are used to repeat instruction
"""
   While Loop Syntax
   while condition:
   Statement
"""
count=1
while (count<=5):
    print("Hello", count)
    count+=1
print("loop ended")

i=7
while(i>1):
    print("Neil", i)
    i-=1
print("Loop Ended")

#break word is used to terminate the loop
coun = 0
while(coun<=10):
    print("MY NAME IS NEIL", coun)
    if(coun==2):
        break
    coun+=1
print("End Of Loop")

#continue terminates execution in the current iteration and continues execution of loop with next iteration
j=0
while (j<=7):
    if(j==4):
        j+=1
        continue
    print("Neil Emmanuel Mathias", j)
    j+=1