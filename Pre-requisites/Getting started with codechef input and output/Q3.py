# How to accept multiple inputs in a line
# Sometimes - we have to accept multiple inputs in a single line.
# The way to accept multiple integers in a single line is to use the split and map function.

# split function breaks the input based on the separator - by default, it splits inputs separated by spaces in a single line into different inputs which you can assign to different variables
# map function converts each input into the defined datatype
# The syntax for the same is as follows -

#  a, b, c = map(int, input().split())   # assigns integer input values to variables a, b and c
# Task
# Now lets try and solve the following

# Accept 3 space separated integers given in a line into 3 variables - 
# A
# A, 
# B
# B and 
# C
# C
# Print them out to a single line on the console
# You can play around with the exact syntax in the IDE -> refer to the solution in case you are unable to get this correct.
# Code the solution in the IDE and then click Submit to continue.

A, B, C = map(int,input().split())
print (A, B, C)