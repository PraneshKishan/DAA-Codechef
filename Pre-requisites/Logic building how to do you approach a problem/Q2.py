# Problem(Farm animals) - Solve sub-components
# How do we find the following?

# Z is divisible only by X
# Z is divisible only by Y
# Z is divisible by both X and Y
# Z is divisible by neitherm X nor Y

#Answer
X = 3
Y = 4
Z = 12
if (Z%X == 0) and (Z%Y == 0):
    print('Z is divisible by both X and Y')
elif (Z%X == 0):
    print('Z is divisible only by X')
elif (Z%Y == 0):
    print('Z is divisible only by Y')
else:
    print('Z is divisible by neither X nor Y')

X = 3
Y = 5
Z = 13
if (Z%X == 0) and (Z%Y == 0):
    print('Z is divisible by both X and Y')
elif (Z%X == 0):
    print('Z is divisible only by X')
elif (Z%Y == 0):
    print('Z is divisible only by Y')
else:
    print('Z is divisible by neither X nor Y')
    
