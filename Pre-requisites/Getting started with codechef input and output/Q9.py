# String mirror - Double strings
# Write a program in the IDE which does the following

# Accepts the count of test cases - 
# t
# t - in the 1st line
# First line of each test case consists of a string 
# S
# S
# You need to perform the following operation
# Create a variable 
# X
# X which contains the string 
# S
# S concatenated with the string 
# S
# S
# Output 
# X
# X for each test case

#Answer

t = int(input())
for i in range(t):
    S = str(input())
    #create a variable X which stores the value of string S concatenated with itself
    X = S + S           
    #output the variable X
    print(X)