# Test cases with multiple types of input
# In the previous problem, each testcase had 2 lines of input - each consisting of integers.
# Test cases can also contain a combination of integers and strings.

# Task
# Lets write a program in the IDE which performs the following

# The 1st line of input contains 
# t
# t - the count of testcases
# Each testcase consists of the following 
# 2
# 2 lines of input
# The 1st line of the testcase contains 2 integers - accept them as variables 
# A
# A and 
# B
# B
# The 2nd line of the testcase contains 1 string - accept it as a variable 
# S
# S
# For each test case, output on one line the 2 integers followed by the string

#Answer

t = int(input())
#run a loop to accept 't' testcases
for i in range(t):
    #accept 2 integers on the 1st line of each test case
    A, B = map(int,input().split())     
    #accept 1 string on the 2nd line of each test case
    C = str(input())
    #output the 2 integers and 1 string on a single line for each test case
    print(A, B, C)       