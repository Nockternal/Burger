﻿#************* HELP *****************
#REMEMBER THAT IF YOU NEED SUPPORT ON ANY ASPECT OF YOUR COURSE SIMPLY LEAVE A
#COMMENT FOR YOUR MENTOR, SCHEDULE A CALL OR GET SUPPORT OVER EMAIL.
#************************************

# ================== Types of Errors ==================
# There are 3 types of errors:
#   - Compilation or syntax errors
#   - Runtime errors
#   - Logical errors


# ================== Compilation Errors ==================
# Compilation errors are also known as syntax errors.
# These errors are due to incorrect syntax used in the program and you will find they are the most common type of error.
# The compiler is able to detect such errors and if these error are present the compilation of the program fails and is terminated.

# ================== Runtime Errors ==================
# Runtime errors occur during the execution of your program.
# Your program will compile but the error occurs while the program is running.
# Examples of what might cause a runtime error are, dividing by zero or referencing a out of range list item.

# ================== Logical Errors ==================
# Logical errors can be the most difficult errors to spot and resolve.
# This is because, as the name implies, the error is related to the logic of the program.
# Logical errors are not detected by the compiler and your program  will compile and run.
# However, they cause the the output of your program to not be what you expected.


# ************ Example 1 ************ 
#Print("Hello World!")
# The statement above is an example of a syntax error.
# As you can see the print keyword has a capital 'P', but  Python is case sensitive so Print and print are two different things.
# Try removing the # from in front of the print statement and run this program; do you see the error?

# ************ Example 2 ************
#word = "Python"
#character = word[6]
# The statement above is an example of a runtime error.
# As you can see, the second statement is referencing an index that is out of bounds.
# Try removing the # from in front of both statements above and run this program; do you see the error?

# ************ Example 3 ************
#areaTrapezoid = 3 + 5 * 6 / 2
#print(areaTrapezoid)
# The statement above is an example of a logical error.
# The code above should calculate the area of a Trapezoid with parallel sides of length 3 and 5, and a height of 6.
# The area of this trapezoid should be 24, but when you run this program, you see that this is not the case.
# This is because of the missing brackets around 3 + 5
# The statement should be:
#       areaTrapezoid = (3 + 5) * 6 / 2



# ****************** END OF EXAMPLE CODE ********************* # 


# == Make sure you have read and understood all of the code in this file.
# == Please complete the compulsory task below to proceed to the next task ===
# == Ensure you complete your work in this folder so that one of our mentors can easily locate and mark it ===




# ======== Compulsory Task 1 =====================
#Follow these steps:
#
#Open ‘errors.py’ in your task folder.
#Attempt to run the program. You will encounter various errors.
#Fix the errors and then run the program.
#Save the corrected file.
#Now run the program and notice the output - fix the error and add comments to the code to indicate which of the three types of errors it was.
#Each time you fix an error, add a comment in the line you fixed it and indicate which of the three types of errors it was.
#Do the same for ‘exampleErrors.py’

# ======= Compulsory Task 2 =====================
#Follow these steps:
#
#Create a new Python file, called ‘logic.py’.
#Write a program that displays a logical error (be as creative as possible!).

# ====== Optional Task =========================
#Follow these steps:
#
#Create a new Python file in this folder called “Optional_task.py.”
#Write a program with two compilation errors, a runtime error and a logical error.
#Next to each error, add a comment that explains what type of error it is and why it occurs.





