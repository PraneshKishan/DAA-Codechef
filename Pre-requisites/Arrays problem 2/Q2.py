# count(), index() functions

# Task
# You are given 
# T
# T test cases

# the 1st line of each test case are 2 integers - 
# N
# N and 
# X
# X
# the 2nd line of each test case contains 
# N
# N space separated integers which form the list 
# A
# A
# For each list 
# A
# A - you need to output the following 
# 2
# 2 integers on a single line

# the occurrence of 
# X
# X in the list 
# A
# A
# the index or the position where 
# X
# X occurs for the 1st time in the list 
# A
# A
# Note: Lists in python are zero indexed. Hence index() of the 1st element will be 
# 0
# 0.


t = int(input())
for i in range(t):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    #variable to store the count of X
    occurrence = A.count(X)
    #variable to store the position / index of X
    index = A.index(X)
    print(occurrence, index)