#print number from 1 to 100
i=1
while(i<=100):
    print("The number is: ", i)
    i+=1
    
#print number from 100 to 1
j=100
while(j>=1):
    print("The number is: ", j)
    j -=1

#print multiplication table of n
n= int(input("The number you want to multiply with: "))
count=1
while(count<=10):
    print(n, "X", count, "=", n*count)
    count+=1
    
#print the element of following list using a loop [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
square = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
count=0
while (count< len(square)):
    print(square[count])
    count+=1
    
#search for a number x in this tuple using loop (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
squares = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x= int(input('The number you want to search for:'))
k=0
while (k < len(squares)):
    if(squares[k]==x):
        print("Number found at index", k)
        break
    k+=1
else:
    print("Number does not exist")
    