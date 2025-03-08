list1=[1, 2, 3]
list2= [1,2,1]
copy_list1=list1.copy()
copy_list1.reverse()
copy_list2=list2.copy()
copy_list2.reverse()
if(copy_list1==list1):
    print(f"{copy_list1} is palindrome")
else:
    print(f"{copy_list1}not a palindrome")
if(copy_list2==list2):
    print(f"{copy_list2} is a palindrome")
else:
    print(f"{copy_list2} is not a palindrome")