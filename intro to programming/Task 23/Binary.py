
def binary_simple(n):
    return int(n, 2)


def binary_complex(y):
    value = 0
    for i in y:
        value = value*2 + int(i)
    return value


binary_input = input("Please enter binary ")

print("This in the simple version result ",binary_simple(binary_input))

print("This in the complex version result ",binary_complex(binary_input))

