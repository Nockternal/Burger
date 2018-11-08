lists = []
total = 0
user = "john"
number = 0


def looper():
    global avarage
    global number
    global total
    while number >= 0:
        number = int(input("Please enter a number"))
        print(number)
        if number >= 0:
            lists.append(number)
    for i in lists:
        total = total + i
    avarage = total / len(lists)


name = input("Please enter your name")
if name == user:
    looper()
    print("The average Number entered is > {}".format(avarage))
else:
    print("You are not a verified user.")



