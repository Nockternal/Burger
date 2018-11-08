# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

print("Welcome to the error program")
print("\n")

ageStr = "24 years old" #I'm 24 years old.

r = ageStr
s = ''.join(x for x in r if x.isdigit())
print(int(s))
age = int(s)

print("I'm ",age," years old.")
three = "3"

answerYears = age + 3

print("The total number of years:" + "answerYears")
answerMonths = answerYears*12
print("In 3 years and 6 months, I'll be " , answerMonths , " months old")

#HINT, 330 months is the correct answer

