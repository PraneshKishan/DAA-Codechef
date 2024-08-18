# del() function
# Next, let us cover the del() function.

# Task
# You are given 
# T
# T test cases

# the 1st line of each test case are 2 integers - 
# N
# N and 
# X
# X (
# 1
# ≤
# X
# ≤
# N
# 1≤X≤N)
# the 2nd line of each test case contains 
# N
# N space separated integers which form the list 
# A
# A
# For each list 
# A
# A - you need to use the 
# d
# e
# l
# (
# )
# del() function to delete the element at the 
# X
# t
# h
# X 
# th
#   position and output the resulting 
# N
# −
# 1
# N−1 space separated integers.

# Note: There are other functions similar to del() in python such as remove(), pop(), clear() - you should check out their syntax and usage as well

#Answer
t = int(input())#3
for i in range(t):
    N, X = map(int, input().split())# N = 5, X = 3
    A = list(map(int, input().split()))#1 2 3 2 1 
    #We need to remove the element at the Xth position
    #Python lists are 0 indexed
    del A[X-1]
    #print only the N-1 space separated integers - not the list
    # print(_A)
    for i in range(len(A)):
        print(A[i],'\n')