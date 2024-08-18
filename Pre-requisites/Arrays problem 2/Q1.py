# max(), min() and sum() functions

# Task

# There are 
# T
# T test cases.

# The 1st line of each test case contains the integer 
# N
# N
# The 2nd line of each test case contains 
# N
# N space separated integers denoted as the list 
# A
# A
# For each list, you need to output 3 integers in a single line

# the highest value of the list
# the smallest value of the list
# the sum of all the values of the list

#Answer
t = int(input())
for i in range(t):
    N = int(input())
    A = list(map(int, input().split()))
    #highest element of the list
    highest = max(A)
    #smallest element of the list
    smallest = min(A)
    #sum of all the elements of the list
    total = sum(A)
    print(highest, smallest, total)