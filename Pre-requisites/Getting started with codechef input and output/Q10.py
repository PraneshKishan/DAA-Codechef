# Debug this code - Why is this code incorrect
# So as you solve programming problems - you will need to debug and find errors in your own code.

# Task
# You are given a program which does the following

# Accepts the count of test cases - 
# t
# t - in the 1st line
# The only line of each test case consists of an integer 
# N
# N
# For each test case, output to the console the value that is double the integer 
# N
# N
# Can you try and debug / fix the error in the given program?

#Answer
t = int(input())
for i in range(t):
    N = int(input())
    print(2*N)