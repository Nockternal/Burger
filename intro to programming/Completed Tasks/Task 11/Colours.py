
runners = {"john":95,"jill":105,"jack":115,"james":125,"alice":119,"allen":145}
people = []

fullpro = "Provincial Colours"
halfpro = "Provincial Half Colours"
proscroll = "Provincial Scroll"
procert = "Provincial Certificate"


for i in runners.keys():
    people.append(i)


def awards():
    print("__________________________________________________________")
    for k, v in runners.items():
        if v <= 100:
            print("{} You have earned {}".format(k,fullpro))
        elif v <= 110:
            print("{} You have earned {}".format(k,halfpro))
        elif v <= 115:
            print("{} You have earned {}".format(k,proscroll))
        elif v <= 120:
            print("{} You have earned {}".format(k,procert))
        elif v > 120:
            print("{} Unfortunately you didn't receive a reward".format(k,procert))

    print("__________________________________________________________")


print("List of people who participated")

for p in people:
    print(p)

awards()


