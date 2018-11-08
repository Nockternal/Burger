def add(x,y,z):
    addof = x + y + z
    return addof


def minus(x,y,z):
    minusof = x - y
    return minusof


def multiply(x,y,z):
    multiplyof = z * x
    return multiplyof


def sum(x,y,z):
    sumof = (x + y + z) / z
    return sumof


number1 = int(input("Please enter First number"))
number2 = int(input("Please enter Second number"))
number3 = int(input("Please enter Third number"))

print(add(number1,number2,number3))
print(minus(number1,number2,number3))
print(multiply(number1,number2,number3))
print(sum(number1,number2,number3))
