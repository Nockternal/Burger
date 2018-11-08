
x = float(input('Enter a number: '))
y = float(input('Enter a number: '))

#i need to see the average of the numbers entered
z = x+y/2
corz = (x+y)/2
print('The average of the two numbers you have entered is:',z)
print("Corrected answer is : ",corz)

#this is a logic error example where the coder is not applying the order of opperation to the calculation

product = 0
for i in range(10):
    product *= i

# 0 x 0 is a logic error

nums = 0
for num in range(10):
    num += num
    print(num)
#this is a potential tricky one where this cound have been the intended outcome to count evens. but it
#seems like an error because they starting point count 0+0
