# Problem(High Accuracy)- Solve the complete problem
# There are 
# 100
# 100 questions in a paper.

# Each question carries +3 marks for correct answer,
# -1 marks for incorrect answer i.e. one mark is deducted for each incorrect answer,
# 0 marks for an unattempted question.
# It is given that Chef received exactly 
# X
# X 
# (
# 0
# ≤
# X
# ≤
# 100
# )
# (0≤X≤100) marks.
# Determine the minimum number of problems Chef marked incorrect.

# Input Format
# First line will contain 
# T
# T, number of test cases. Then the test cases follow.
# Each testcase contains of a single integer 
# X
# X, marks that Chef received.
# Output Format
# For each test case, output the minimum number of problems Chef marked incorrect.

#Answer


t = int(input())            
for i in range(t):          
    X = int(input())
    if X%3 == 0:
        print(0)
    elif (X+1)%3 == 0:
        print(1)
    else:
        print(2)

