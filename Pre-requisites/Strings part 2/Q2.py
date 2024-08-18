#Numerical characters in strings

t = int(input())#2
for i in range(t):
    A = input()#1005
    B = input()#5001
    
    i = 0 
    n = len(A)#4
    #Flag is a very imporant tool in programming problems - you will come across various examples in later problems as well
    flag = 0
    
    while i<n:
        #Checking A from left to right and B from right to left
        if A[i]==B[n-i-1]:      
            i = i + 1
        else:
            #If specific character in A and B do not match, then they cannot be reverse of each other
            flag = 1
            break
    
    if flag==1:
        print('NO')
    else:
        print('YES')