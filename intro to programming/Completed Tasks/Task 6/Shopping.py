items = []
prices = []
diction = {}
total = 0

for i in range(0,3):
    string = input("please enter product name")
    num = float(input("Please enter the cost of this product"))
    diction[string] = num
    items.append(string)
    prices.append(num)


for i in prices:
    total = total + i

count = len(prices)
avarage = total / count

print("Your list of items are:")
for i in items:
    print(i)

print("Total Items list Price is {}".format(total))
print("The avarage Price for all items are {}".format(avarage))
