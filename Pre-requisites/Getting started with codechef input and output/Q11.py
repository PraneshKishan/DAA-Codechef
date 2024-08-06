# Debug this code - Why is this code incorrect
# Now try and debug this problem.

# You are given a program in the IDE which is trying to do the following

# Accepts the count of test cases - 
# t
# t - in the 1st line
# Each line of test case consists of an integer 
# N
# N
# For each test case, it is supposed to print double the integer 
# N
# N as the output

t = int(input())
for i in range(t):
    N = int(input())
    print(2*N)