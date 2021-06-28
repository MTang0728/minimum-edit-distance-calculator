# import library
import sys
import numpy as np
# get user input for source string and target string
source = sys.argv[1]
target = sys.argv[2]
# define functions for calculating Levenshtein distance
# define delete cost
def del_cost(char):
    return 1
# define insert cost
def ins_cost(char):
    return 1
# define substitute cost        
def sub_cost(source_char, target_char):
    if source_char == target_char:
        return 0
    else:
        return 2
# Initialization: the zeroth row and column is the distance from the empty string
n = len(source)
m = len(target)
d = np.zeros((n+1, m+1))
for i in range(1, n+1):
    d[i, 0] = d[i-1, 0] + del_cost(source[i-1])
    pass
for j in range(1, m+1):
    d[0, j] = d[0, j-1] + ins_cost(target[j-1])
    pass
# Recurrence relation:
for i in range(1, n+1):
    for j in range(1, m+1):
        d[i, j] = min(d[i-1, j] + del_cost(source[i-1]),
                      d[i-1, j-1] + sub_cost(source[i-1], target[j-1]),
                      d[i, j-1] + ins_cost(target[j-1]))
        pass
    pass
# print result
min_distance = d[n, m]
print('Minimum Edit Distance: ', int(min_distance))
