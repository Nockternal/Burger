
print("Task 1")

number = int(input("Please enter a number"))
amount = int(input("How how would you like the times table to run"))

for i in range(1,(amount+1)):
    print(number, " x ", i, "=", (number * i))

print("Task 2")

year = int(input("Please enter starting year"))
endyear = int(input("Please enter how many years you want to check for"))

count = year + endyear + 1
for i in range(year,count):
    if i % 4 == 0 and i % 100 != 0:
        print(i, " is a leap year.")
    elif i % 4 != 0:
        print(i, " is not a leap year.")