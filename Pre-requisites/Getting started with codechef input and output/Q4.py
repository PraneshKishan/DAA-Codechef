#  How to accept multiple integers on separate lines
# Let's make this a little bit more complicated.

# You need to write a program which does the following

# Accepts 
# 2
# 2 integers as input in 1st line as the variables 
# A
# A, 
# B
# B
# Accepts 
# 3
# 3 integers as input in the 2nd line as the variables 
# C
# C, 
# D
# D and 
# E
# E
# Accepts 
# 4
# 4 integers as input in the 3rd line as the variables 
# F
# F, 
# G
# G, 
# H
# H and 
# I
# I
# Prints out 
# 9
# 9 integers as output in a single line to the console
# Code the solution in the IDE and then click Submit to continue.

#Answer
A, B = map(int,input().split())
C, D, E = map(int, input().split())
F, G, H, I = map(int,input().split())
print(A, B, C, D, E, F, G, H, I)