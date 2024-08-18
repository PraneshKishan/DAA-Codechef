#Practice problem - Count the Holidays

t = int(input())#3
for i in range(t):
    N = int(input())#2 - no of festival holidays
    A = list(map(int, input().split()))# 5 7
    
    weekend = [6,7,13,14,20,21,27,28]

    overall = A + weekend

    overall_unique = list(set(overall))
    print(len(overall_unique))  