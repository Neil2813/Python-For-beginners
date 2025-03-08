#for loop is used for traversing list dictionary tuples set
list1 = ["neil", "Neil", "NEil", "NEIl"]
str = "Neil Emmanuel Mathias"
for neil in list1:
    print(neil)
for NEIL in  str: #it will print individual character
    print(NEIL)

list2 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x=int(input("Number:"))
idx=0
for val in list2:
    if(val==x):
        print("Number found at index", idx)
    idx +=1
