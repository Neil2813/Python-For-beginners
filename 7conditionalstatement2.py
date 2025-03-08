light=input("Enter the traffic light?")
if(light=="red"):
    print(f"The light is {light}. You need to stop!!!")
elif(light=="yellow"):
    print(f"The light is {light}. You need to get ready..")
elif(light=="green"):
    print(f"The light is {light}, Hurray you can go!!")
else:
    print(f"{light} doesnt exist")