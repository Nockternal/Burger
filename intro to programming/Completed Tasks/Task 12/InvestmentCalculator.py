import math
#tests
#print(1000 * math.pow((1+(8/100)),1))
#print(1000*(1+(8/100)*1))

p = float(input("Please enter iniial investment amount"))
i = float(input("Please enter interest rate"))/100
t = float(input("Please enter investment term in years"))
interest = input("Please specify type of interest (simple/compound)")


def compound():
    print(p * math.pow((1+i),t))


def simple():
    print(p*(1+i*t))


if interest == "simple":
    print(simple())


elif interest == "compound":
    print(compound())

