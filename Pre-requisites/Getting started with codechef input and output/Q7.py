# Test cases with multiple lines of input
# In the previous problem, we had 
# t
# t test cases and each test case had 1 line of input.
# However, each test case can have multiple lines of input as well.

# Task
# Lets write a program in the IDE which performs the following

# The 1st line of input is an integer 
# t
# t - the count of test cases
# Each test case consists of 2 lines of input
# The 1st line of input has 2 space separated integers - accept them as variables 
# A
# A and 
# B
# B
# The 2nd line of input has 3 space separated integers - accept them as variables 
# C
# C, 
# D
# D and 
# E
# E
# For each test case - output all integers on a single line

#Answer
t = int(input())       
#run a loop to accept 't' inputs
for i in range(t):     
    #accept 2 integers on the 1st line of each test case
    A, B = map(int,input().split())      
    #accept 3 integers on the 2nd line of each test case
    C, D, E = map(int,input().split())   
    #output the 5 integers on a single line for each test case    
    print(A, B, C, D, E)