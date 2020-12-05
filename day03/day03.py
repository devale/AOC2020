#import re #regex
import os

LOGGING = 0

def log(s):
    if LOGGING:
        print( str(s) )



os.chdir(r'D:/GIT/AOC2020-1')

with open('day03/input.txt', mode='r') as f:
    f_list = f.read().splitlines() #better than readlines() as it removes \n

#approach 1:
# width: 32, and positions: 1 4 7 10 13 16 19 22 25 28 31. 2 5 8...etc
# that means that every 3 runs, a position will be hit again. 

# len: 323. 
# 3 steps right, 1 step down, means we are moving 3x323 in width = 969
# 969 / 32 = 30.2 
# 1. replace dot with 0, # with 1.
# 2. the pattern should exist horizontally 31 times, so duplicate 30 times
# 3. and each position will be taken 10 times.
# 4. the last 3 rows will repeat the first 3 rows. 

#approach 2:
# use iterator to get l_num and line. l_num can be used for horizontal position with modulus to calculate the next horizontal position (%32), subtract 1 for 0-based index
# loop through lines, to get string of chars. 
# count X in string.

line_length = len(f_list[0])
log(f'line count: %d' % len(f_list))
log(f'line length: %d' % len(f_list[0]) )


def run_down(step_right, step_down):
    current_line = 0
    tree_count = 0
    for l_num , l in enumerate(f_list[:
        ]):
        if l_num != current_line:
            continue
        log(f'l_num: %d' % l_num)
        log(f'line: %s' % l)
        h_pos =  ( step_right * l_num // step_down) % line_length # 32 becomes 0
        log(f'h_post: %d' % h_pos )
        char = l[h_pos]
        log(F'char found: %s' % char) 
        if char == '#':    #zero index 
            tree_count += 1
        
        current_line += step_down

    print(f'number of trees ran into: %d' % tree_count)
    return tree_count
#part 1
#run_down(3, 1)

#part 2: find number of tree hits when taking other slopes
# Right 1, down 1: 85
# Right 3, down 1: 176
# Right 5, down 1: 96
# Right 7, down 1: 87
# Right 1, down 2: 40
# final answer = multiple results
slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
result = 1
for slope in slopes:
    result *= run_down(slope[0],slope[1])
print(f'the total multiple = %d' % result)


