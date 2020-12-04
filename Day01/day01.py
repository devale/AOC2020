import os
from itertools import combinations

os.chdir(r'D:/GIT/AOC2020-1')

with open('day01/input.txt', mode='r') as f:
    numlist = list(map(int, f.readlines() ))

#print(os.getcwd() )
#print(len(numlist)) 

#part 1
#combo = [[ x * y for x in numlist if x+y==2020 ] for y in numlist ]
#result = []
#for i in combo:
#    if i:
#        result.append(i)
#print(result)

#part 2
triple = [[[ x * y * z for x in numlist if x+y+z==2020 ] for z in numlist] for y in numlist ]
result = []
for i in triple:
    for j in i:
        if j:
            result.append(i)
print(result)

#better by sgraaf:
#print('--- Part Two ---')
#for i, j, k in combinations(numlist, 3):
#    if i + j + k == 2020:
#        print(f'{i} + {j} + {k} = 2020')
#        print(f'{i} * {j} * {k} = {i * j * k}')
#        break  # early stopping condition
#else:  # early stopping condition not reached
#    print('Could not find three entries that sum to 2020')

#better 2: create set_num, for each num in list, if 2020-num in set_num. 