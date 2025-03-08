A=int(input("Value of A: "))
G=input("M or F: ")
if((A==1 or A==2) and G=="M"):
    print("The fee is 100")
elif((A==3 or A==4) and G=="F"):
    print("The fee is 200")
elif(A==5 and G=="M"):
    print("The fee is 300")
else:
    print("There is no fee")