#Create a list of ord values of a string

t = int(input())#3
for i in range(t):
    S = input()#abc
    A = []
    
    for i in S:
        #Converts a character into its ASCII value
        A.append(ord(i))    
    
    print(*A)