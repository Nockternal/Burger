string = "abcdefg hijklmnop"
#string = "Hello World"


for i in string[::2]:
    if i != " ":
        x = i.upper()
        string = string.replace(i, x)
print(string)





