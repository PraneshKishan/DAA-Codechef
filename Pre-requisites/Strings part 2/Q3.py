#Practice problem - Wordle

t = int(input())
for i in range(t):
    S = input()
    T = input()
    
    i = 0
    op = ''

    while i < len(T):
        if S[i] == T[i]:
            op += 'G'
        elif S[i] != T[i]:
            op += 'B'
        i += 1
    
    print(op)