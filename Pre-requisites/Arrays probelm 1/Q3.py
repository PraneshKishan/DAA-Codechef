# Practice problem - Penalty Shots
# Using your current knowledge of arrays - you can solve the following problem!

# Task
# It's the soccer match finals in Chefland and as always it has reached the penalty shootouts.

# Each team is given 
# 5
# 5 shots to make and the team scoring a goal on the maximum number of shots wins the game.
# If both the teams' scores are equal, then the game is considered a draw and we would have 
# 2
# 2 champions.
# Given ten integers 
# A
# 1
# ,
# A
# 2
# ,
# …
# ,
# A
# 10
# A 
# 1
# ​
#  ,A 
# 2
# ​
#  ,…,A 
# 10
# ​
#  , determine the winner or find if the game ends in a draw.

# the odd indexed integers(
# A
# 1
# ,
# A
# 3
# ,
# A 
# 1
# ​
#  ,A 
# 3
# ​
#  , 
# A
# 5
# ,
# A 
# 5
# ​
#  , 
# A
# 7
# ,
# A
# 9
# A 
# 7
# ​
#  ,A 
# 9
# ​
#  ) represent the outcome of the shots made by team 
# 1
# 1
# the even indexed integers(
# A
# 2
# ,
# A
# 4
# ,
# A
# 6
# ,
# A
# 8
# ,
# A
# 10
# A 
# 2
# ​
#  ,A 
# 4
# ​
#  ,A 
# 6
# ​
#  ,A 
# 8
# ​
#  ,A 
# 10
# ​
#  ) represent the outcome of the shots made by team 
# 2
# 2
# Note that here 
# A
# i
# =
# 1
# A 
# i
# ​
#  =1 indicates that it's a goal and 
# A
# i
# =
# 0
# A 
# i
# ​
#  =0 indicates a miss.

# Input Format
# The first line of input contains a single integer 
# T
# T denoting the number of test cases. The description of 
# T
# T test cases follows.
# The first and only line of each test case contains ten space-separated integers 
# A
# 1
# ,
# A
# 2
# ,
# …
# ,
# A
# 10
# A 
# 1
# ​
#  ,A 
# 2
# ​
#  ,…,A 
# 10
# ​
#  .
# Output Format
# For each test case, print a single line containing one integer - 
# 0
# 0 if the game ends in a draw or 
# 1
# 1 if the first team wins or 
# 2
# 2 if the second team wins.

t = int(input())#4
for i in range(t):
    A = list(map(int,input().split()))# 0 0 0 0 0 0 0 0 0 0 
    #Calculate and store Team-1 and Team-2 scores
    team1 = A[0] + A[2] + A[4] + A[6] + A[8]
    team2 = A[1] + A[3] + A[5] + A[7] + A[9]
    
    #Apply relevant conditions to check for victory
    if team1 > team2:
        print(1)
    elif team1 < team2:
        print(2)
    else:
        print(0)
    