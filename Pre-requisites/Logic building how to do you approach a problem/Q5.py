# Problem 3 (High Accuracy) - Solve sub-components
# How do we find the number of questions incorrectly solved?

# X is divisible by 3, then minimum number of questions incorrect is 0

# X+1 is divisible by 3, then minimum number of questions incorrect is 
# 1
# 1
# If 
# X
# +
# 2
# X+2 is divisible by 3, then minimum number of questions incorrect is 
# 2
# 2
# Go ahead and code out this sub-problem in the IDE!

#Answer

X = 30
if X % 3 == 0:
    print('Number of questions incorrctly solved is 0')
elif (X+1)%3 == 0:
    print('Number of questions incorrctly solved is 1')
else:
    print('Number of questions incorrctly solved is 2')
    
X = 34
if X%3 == 0:
    print('Number of questions incorrctly solved is 0')
elif (X+1)%3 == 0:
    print('Number of questions incorrctly solved is 1')
else:
    print('Number of questions incorrctly solved is 2')