data = []

name = None


while name != "John":

    name = input("Enter your Name :  ")
    if name != "John":
        data.append(name)
    else:
        pass


print("Incorrect Name that have been given")
for i in data:
    print(i)
