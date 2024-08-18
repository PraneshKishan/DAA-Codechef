# Debug this code - Non-Negative Product
# Alice has an array of 
# N
# N integers — 
# A
# 1
# ,
# A
# 2
# ,
# …
# ,
# A
# N
# A 
# 1
# ​
#  ,A 
# 2
# ​
#  ,…,A 
# N
# ​
#  .
# She wants the product of all the elements of the array to be a non-negative integer.
# That is, it can be either 
# 0
# 0 or positive. But she doesn't want it to be negative.

# To do this, she is willing to remove some elements of the array.
# Determine the minimum number of elements that she will have to remove to make the product of the array's elements non-negative.


#Answer
t = int(input())
for i in range(t):
    n = int(input())#3
    A = list(map(int,input().split())) # 2 -1 -1 100
    
    count_neg = 0 #2
    count_zero = A.count(0) 
    
    if count_zero > 0:
        print(0)
    else:
        i = 0
        while i<n:#0 2<4
            if A[i] < 0: 
                count_neg = count_neg + 1
            i = i + 1
        
        if count_neg%2 > 0:
            print(1)
        else:
            print(0)