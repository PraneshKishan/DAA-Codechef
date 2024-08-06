# Count positive and non-zero elements

# Given N space separated integers and an integer k, please perform the following operations

# Store the integers in the array A
# Count all the items of the array A strictly greater than 0 and store it as the variable pos
# Count all the items of the array A strictly lesser than 0 and store it as the variable neg
# Count all items of the 
# A which are divisible by k and store it as the variable divk

# Input Format
# The first line of input will contain a single integer T, denoting the number of test cases.
# Each test case consists of a two lines of input
# The 1 st line of input contains the integers N and k
# 2 nd line of input contains 
# N space separated integers - denoting the array A


t = int(input())
for i in range(t):
    N, k = map(int, input().split())
    A = list(map(int, input().split()))
    

    pos = 0
    neg = 0
    divk = 0
    
    i = 0
    while i<N:
        if A[i] <  0:
            neg = neg + 1

        elif A[i] >  0:
            pos = pos + 1
            
        if A[i] == 0:
            divk = divk + 1
        i = i + 1
    
    print(pos,neg,divk)
