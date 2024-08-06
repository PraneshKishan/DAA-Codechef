# Array construction

# Let us start with the very basics of array construction and manipulation.

# Task
# Given an integer N, create an array A of length consisting of the first N  integers -
# [1,2,3,...,N].

# You need to output the following
# - Output the array A 
# - Output only the values of array A
# - Output the array A sorted in a descending order

# Input Format
# - The first line of input will contain a single integer T, denoting the number of test cases.
# - Each test case consists of a single line of input - the integer N. 

t = int(input())
for i in range(t):
    N = int(input())#3
    A = []
    x = 1
    for i in range(N):
        A.append(x)
        x += 1
    #print the array A
    print(A)              
    #print only the elements from array A
    print(*A)               
    A.sort(reverse = True)
    #print the array A sorted in descending order
    print(A)                